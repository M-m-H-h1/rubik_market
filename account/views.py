import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from datetime import timedelta
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import TemplateView, FormView, UpdateView, ListView, CreateView
from .compare_module import CompareProduct
from cart.models import Order, OrderItem
from products.favorite_module import FavoriteProduct
from products.models import Products
from . import forms
from .models import ContactUs, Us_Team, Message, Code_Password_Recovery, Profile, Address, City
from django.core.mail import send_mail


class RgisterUserView(FormView):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home:main')

        return super().get(request, *args, **kwargs)

    template_name = 'account/register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('home:main')

    def form_valid(self, form):
        form_date = form.cleaned_data
        user = User.objects.create_user(username=form_date['username'], password=form_date['password2'],
                                        email=form_date['email'])
        login(self.request, user)
        messages.success(self.request, 'حساب کاربری شما با موفقیت ساخته شد !', extra_tags='alert alert-success')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'عملیات ناموفق !!', extra_tags='alert alert-danger')
        return super().form_invalid(form)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            messages.success(request, 'شما با موفقیت به حساب خود ورود کردید ', extra_tags='alert alert-success')
            return redirect('home:main')
        else:
            messages.error(request, 'عملیات ناموفق', extra_tags='alert alert-danger')
    else:

        form = forms.LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')


class ContactUsView(TemplateView):
    template_name = 'account/cntactus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = ContactUs.objects.all()
        context['us_team'] = Us_Team.objects.all()
        return context


class MessageView(FormView):
    template_name = 'account/message.html'
    form_class = forms.MessageForm
    success_url = reverse_lazy('home:main')

    def form_valid(self, form):
        form_date = form.cleaned_data
        user = self.request.user
        user_email = self.request.user.email
        user_name = self.request.user.get_full_name()

        form_date['user'] = user
        form_date['email'] = user_email
        form_date['name'] = user_name

        Message.objects.create(**form_date)
        messages.success(self.request, 'پیام شما با موفقیت ارسال شد', extra_tags='alert alert-success')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'عملیات ناموفق', extra_tags='alert alert-danger')
        return super().form_invalid(form)

class Password_Recovery(FormView):
    template_name = 'account/password_recovery.html'
    form_class = forms.PasswordResetForm
    success_url = reverse_lazy('account:verify-code')






    def form_valid(self, form):
        email = form.cleaned_data['email']
        code = random.randint(10000, 99999)
        Code = Code_Password_Recovery.objects.filter(email=email)

        if Code:
            Code.delete()

        s_email = self.request.session['recovery_email'] = email



        current_time = timezone.localtime(timezone.now())
        five_minutes_later = current_time + timedelta(seconds=300)
        Code_Password_Recovery.objects.create(code=code, email=email, expiration_time=five_minutes_later)

        recipient_list = [form.cleaned_data['email']]
        subject = 'This message is from the Rubik Market site'
        message = f'this is code for recovery your password \n {code}'
        from_email = 'admin@mysite.com'
        send_mail(subject, message, from_email, recipient_list)
        messages.success(self.request, f'با موفقیت به {email} ارسال شد .', extra_tags='alert alert-success')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'عملیات ناموفق', extra_tags='alert alert-danger')
        return super().form_invalid(form)

class VerifyCodeView(View):

    def dispatch(self, request, *args, **kwargs):
        email = request.session.get('recovery_email')
        if not Code_Password_Recovery.objects.filter(email=email).exists():
            return redirect('home:main')
        return super().dispatch(request, *args, **kwargs)


    def get(self, request):
        return render(request, 'account/verify-code.html')

    def post(self, request):
        error = ""
        if request.method == 'POST':
            one = request.POST.get('one')
            two = request.POST.get('two')
            three = request.POST.get('three')
            four = request.POST.get('four')
            five = request.POST.get('five')
            number = int(str(one) + str(two) + str(three) + str(four) + str(five))

            current_time = timezone.localtime(timezone.now())
            try:
                recovery_code = Code_Password_Recovery.objects.get(code=number)
                if recovery_code.expiration_time >= current_time.time():
                    user = User.objects.get(email=recovery_code.email)
                    login(request, user)
                    self.request.session['is_authenticated_to_see_fp'] = True
                    self.request.session.delete('recovery_email')

                    recovery_code.delete()
                    messages.success(self.request, 'عملیات موفق !', extra_tags='alert alert-success')
                    return redirect(reverse_lazy('account:forget_password'))
                else:
                    error = 'کد شما منقضی شده است دوباره امتحان کنید'
                    messages.error(self.request, 'عملیات ناموفق', extra_tags='alert alert-danger')
            except Code_Password_Recovery.DoesNotExist:
                error = 'کدی که وارد کردید اشتباه می‌باشد'
                messages.error(self.request, 'عملیات ناموفق', extra_tags='alert alert-danger')

        return render(request, 'account/verify-code.html', context={'errors': error})

class Forget_Password(LoginRequiredMixin, FormView):
    template_name = 'account/forget_password.html'
    form_class = forms.ForgetPasswordForm
    success_url = reverse_lazy('home:main')

    def get_template_names(self):
        if self.request.session.get('is_authenticated_to_see_fp')== True:
            return ['account/forget_password.html']
        else:
            return ['account/404_error.html']

    def handle_no_permission(self):
        return redirect('home:main')

    def form_valid(self, form):
        new_password = form.cleaned_data['new_password']

        user = User.objects.get(username=self.request.user.username)
        user.set_password(new_password)
        user.save()
        login(self.request,user)
        self.request.session['is_authenticated_to_see_fp'] = False
        messages.success(self.request, 'رمز عبور شما با موفقیت تغیر کرد', extra_tags='alert alert-success')
        return redirect(reverse_lazy('home:main'))

    def form_invalid(self, form):
        messages.error(self.request, 'عملیات ناموفق', extra_tags='alert alert-danger')
        return super().form_invalid(form)

class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = 'account/change_password.html'
    form_class = forms.ChangePasswordForm
    success_url = reverse_lazy('home:main')




    def handle_no_permission(self):
        return redirect('home:main')

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['request'] = self.request
        return form_kwargs

    def form_valid(self, form):
        new_pass = form.cleaned_data.get('new_password')
        user = self.request.user
        user.set_password(new_pass)
        user.save()
        login(self.request,user)
        messages.success(self.request, 'رمز عبور شما با موفقیت تغیر کرد !', extra_tags='alert alert-success')

        return redirect('home:main')


    def form_invalid(self, form):
        messages.error(self.request, 'عملیات ناموفق', extra_tags='alert alert-danger')
        return super().form_invalid(form)





class EditProfileUser(LoginRequiredMixin,TemplateView):
    template_name = 'account/profile_user.html'
    user_form = forms.EditProfileUser
    profile_form = forms.EditImageUser


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_order_user'] = Order.objects.filter(user=self.request.user).last()
        return context


    def handle_no_permission(self):
        return redirect('account:login_user')

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = forms.EditProfileUser(post_data, instance=request.user)

        if hasattr(request.user, 'image'):
            profile_form = forms.EditImageUser(post_data, file_data, instance=request.user.image)
        else:
            profile_form = forms.EditImageUser(post_data, file_data)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()  # ذخیره تغییرات بر روی کاربر
            if hasattr(request.user, 'image'):
                if profile_form.has_changed():
                    profile_form.save()  # ذخیره تغییرات بر روی تصویر
            else:
                profile = profile_form.save(commit=False)
                profile.user = request.user  # تنظیم کاربر مرتبط با تصویر
                profile.save()  # ذخیره تصویر جدید

            messages.success(request, 'اطلاعات با موفقیت ویرایش شد', extra_tags='alert alert-success')
            return HttpResponseRedirect(reverse_lazy('account:profile_user'))

        context = self.get_context_data(user_form=user_form, profile_form=profile_form)
        return self.render_to_response(context)


        context = self.get_context_data(user_form=user_form,profile_form=profile_form)

        return self.render_to_response(context)

    def get(self,request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



class DeleteUserImage(View):
    def post(self, request):
        user = request.user
        user.image.image.delete()
        user.save()


class AddAddressView(View):
    def post(self,request):
        form = forms.AddressCreationForm(request.POST,request=request)

        if form.is_valid():
            addr_count = Address.objects.filter(user_id=request.user.id).count()
            if addr_count > 5:
                messages.error(request, 'شما بیشتر از 5 آدرس دارید. لطفاً برخی از آدرس‌ها را حذف کنید.',extra_tags='alert alert-danger')
                return render(request, 'account/add_address.html', {'form': form})
            else:
                address = form.save(commit=False)
                address.user = request.user
                address.save()
                messages.success(request, 'آدرس شما موفقیت ثبت شد', extra_tags='alert alert-success')
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('account:add_address')
        return render(request, 'account/add_address.html', {'form': form})



    def get(self,request):
        success_message = request.session.pop('success_message', None)
        if success_message:
            messages.success(request, success_message, extra_tags='alert alert-success')
        form = forms.AddressCreationForm()
        return render(request,'account/add_address.html',{'form':form})



class DeleteAddressView(View):
    def post(self,request,pk):
        addr = Address.objects.get(id=pk)
        addr.delete()
        messages.success(request, 'آدرس شما با موفقیت حذف شد', extra_tags='alert alert-success')
        return redirect('account:add_address')



class AddressUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        addr = get_object_or_404(Address, pk=pk)
        form = forms.AddressCreationForm(instance=addr,request=request)
        return render(request, 'account/edit_address.html', {'form': form})


    def post(self, request, pk):
        addr = get_object_or_404(Address, pk=pk)
        form = forms.AddressCreationForm(request.POST, instance=addr,request=request)
        if form.is_valid():
            form.save()
            messages.success(request, 'آدرس شما با موفقیت تغیر یافت', extra_tags='alert alert-success')
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(reverse('account:add_address') + '#addresses')
        return render(request, 'account/edit_address.html', {'form': form})

# AJAX
def Load_Cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id)
    return render(request, 'account/city_dropdown_list_options.html', {'cities': cities})




class UserFactorsView(View):
    def get(self,request):
        user = request.user
        order = Order.objects.filter(user=user).order_by('-created_at')
        order_count = order.count()
        paid_orders = Order.objects.filter(user=user,is_paid=True)[:1]
        paid_orders_count = Order.objects.filter(user=user,is_paid=True).count()
        dont_paid_orders = Order.objects.filter(user=user,is_paid=False)


        page_number = request.GET.get('page')
        order_paginator = Paginator(order, 3)
        order_list = order_paginator.get_page(page_number)


        return render(request,'account/user_factors.html',{'order_count':order_count,'orders':order_list,'paid_order':paid_orders,'dont_paid_order':dont_paid_orders,'total_obj':paid_orders_count})

def load_more(request):
    offset = request.GET.get('offset')

    offset_int = int(offset)
    limit = 1

    order_obj = list(Order.objects.filter(user=request.user,is_paid=True).values()[offset_int:offset_int+limit])



    data = {
        'orders': order_obj,

    }
    return JsonResponse(data=data)

class DeleteFactorView(View):
    def get(self,request,pk):
        order = Order.objects.get(id=pk)
        order.delete()
        messages.success(request, 'سفارش شما با موفقیت حذف شد', extra_tags='alert alert-success')
        return redirect('account:user_factors')


class FavoriteProductDetailView(View):
    def get(self, request):
        fav = FavoriteProduct(request)
        return render(request, 'account/favorite_product.html', {'fav': fav})


class AddFavoriteProduct(View):
    def post(self, request, pk):
        product = get_object_or_404(Products, id=pk)
        fav = FavoriteProduct(request)
        fav.add(product=product)
        messages.success(request, 'محصول شما با موفقیت به علاقه مندی ها اضافه شد', extra_tags='alert alert-success')
        return redirect('account:fav_detail')


class FavDeleteView(View):
    def get(self, request, id):
        fav = FavoriteProduct(request)
        fav.delete(id)
        messages.success(request, 'محصول شما با موفقیت از علاقه مندی ها پاک شد', extra_tags='alert alert-success')
        return redirect('account:fav_detail')
