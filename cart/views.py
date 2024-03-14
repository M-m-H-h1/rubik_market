from decimal import Decimal
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from account.models import Address
from .cart_module import Cart
from products.models import Products, Color, Memory
from .models import Order, OrderItem, DiscountCode
from products.favorite_module import FavoriteProduct

class CartDetailView(View):

    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart_detail.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Products, id=pk)
        col = request.POST.get('selected_color')
        color = Color.objects.get(color=col).get_color_display()
        quantity = request.POST.get('quantity')
        memory = request.POST.get('memory_select')
        cart = Cart(request)
        cart.add(product=product, quantity=quantity, color=color, memory=memory)
        return redirect('cart:detail')




class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:detail')


class OrderDetailView(LoginRequiredMixin, View):
    def handle_no_permission(self):
        return redirect('account:login_user')

    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        if order.is_paid == True :
            return render(request,'cart/success_pey.html')
        request.session['order_id'] = str(order.id)

        addr = Address.objects.filter(default=True, user=request.user)
        return render(request, 'cart/order_detail.html', {'order': order, 'addr': addr})


class OrderCreationView(LoginRequiredMixin, View):
    def handle_no_permission(self):
        return redirect('account:login_user')

    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total_price(),
                                     total_discount=cart.total_discount(), total_price_af_dis=cart.final_price_total())

        for product in cart:
            try:
                color = Color.objects.get(color=product['color'])
            except Color.DoesNotExist:
                color = None

            try:
                memory = Memory.objects.get(memory=product['memory'])
            except Memory.DoesNotExist:
                memory = None

            OrderItem.objects.create(order=order, product=product['product'], color=color,
                                     memory=memory, quantity=product['quantity'], price=product['price'],
                                     final_price=product['total'])
        cart.remove_cart()
        return redirect('cart:order_detail', order.id)


class SuccessPeyView(View):
    def get(self,request):
        order_id = request.session.get('order_id')
        order = Order.objects.get(id=int(order_id))
        order.is_paid = True
        order.save()
        self.request.session.delete('order_id')
        return render(request,'cart/success_pey.html')



class ApplyDiscountView(LoginRequiredMixin, View):
    def handle_no_permission(self):
        return redirect('account:login_user')

    def post(self, request, pk):
        code = request.POST.get('discount_code')
        order: Order = get_object_or_404(Order, id=pk)
        try:
            discount_code = DiscountCode.objects.get(name=code)
        except DiscountCode.DoesNotExist:
            messages.error(request, 'کد تخفیف شما اشتباه میباشد .', extra_tags='alert alert-danger')
            return redirect('cart:order_detail', order.id)


        if discount_code.quantity == 0:
            messages.error(request,f'کد تخفیف شما منقضی شده است .',extra_tags='alert alert-danger')
            return redirect('cart:order_detail', order.id)
        total_price_af_dis = Decimal(order.total_price_af_dis)
        discount = Decimal(discount_code.discount)
        order.total_discount_code = total_price_af_dis * discount / 100
        order.total_price_af_dis = str(total_price_af_dis - total_price_af_dis * discount / 100)
        order.save()

        discount_code.quantity -= 1
        discount_code.save()
        messages.success(request,f'کد تخفیف شما با موفقیت عمل کرد. از مقدار کل سفارش شما {discount_code.discount} درصد کم شد .',extra_tags='alert alert-success')
        return redirect('cart:order_detail', order.id)




def top_bar(request):
    products = Products.objects.all()

    context = {
        'test': products
    }

    return render(request, 'includes/top_bar.html', context)


