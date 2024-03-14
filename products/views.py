from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseNotAllowed, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView ,ListView , TemplateView
from django.contrib import messages

from blog.models import Blog
from .models import Products, Top_Product, Special_Sale, Comment, Category , Mark

import requests


def delete_Special_Sale(request, id):
    if request.method == 'POST':
        obj = get_object_or_404(Special_Sale, pk=id)
        obj.delete()
        return redirect(reverse_lazy('home:main'))

    else:
        return HttpResponseNotAllowed([''])



class ProductDetailView(DetailView):
    template_name = 'product_details.html'
    model = Products

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        body = request.POST.get('body')
        user = request.user
        parent_id = request.POST.get('parent_id')
        if parent_id == 0 or not parent_id:
            messages.success(request, f'نظر شما با موفقیت ایجاد شد', extra_tags='alert alert-success')
        else:
            comment = Comment.objects.get(id=parent_id)
            messages.success(request, f'نظر شما در جواب به کاربر {comment.user.username} با موفقیت ایجاد شد',extra_tags='alert alert-success')

        Comment.objects.create(product=product,user=user,body=body,parent_id=parent_id)
        return redirect('product:detail_product',product.slug)






    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_products'] = Top_Product.objects.all()
        return context




def Product_List(request):
    product = Products.objects.all()
    category_list = Category.objects.filter(products__isnull=False).annotate(num_products=Count('products')).order_by('-num_products')

    categories = request.GET.getlist('cat')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    available = request.GET.get('available')

    if categories:
        product = Products.objects.filter(category__name__in=categories).distinct()

    if min_price and max_price:
        product = product.filter(price__lte=max_price, price__gte=min_price).distinct()
    if available:
        product = product.filter(available=True)


    page_number = request.GET.get('page')
    paginator = Paginator(product, 2)
    object_list = paginator.get_page(page_number)

    if request.GET.get('sort') == 'newest':
        products_page = paginator.get_page(page_number)
        sorted_products = sorted(products_page,reverse=True, key=lambda p: p.created_at )
        return render(request, 'product_list.html', context={'product': sorted_products,'category_list':category_list})

    if request.GET.get('sort') == 'visit':
        products_page = paginator.get_page(page_number)
        sorted_products = sorted(products_page,reverse=True, key=lambda p: p.views)
        return render(request, 'product_list.html', context={'product': sorted_products,'category_list':category_list})

    if request.GET.get('sort') == 'discounts':
       products_page = paginator.get_page(page_number)
       sorted_products = sorted(products_page,reverse=True, key=lambda p: p.discount_percent)
       return render(request, 'product_list.html', context={'product': sorted_products,'category_list':category_list})

    if request.GET.get('sort') == 'Inexpensive':
        products_page = paginator.get_page(page_number)
        sorted_products = sorted(products_page, key=lambda p: p.price)
        return render(request, 'product_list.html', context={'product': sorted_products,'category_list':category_list})


    return render(request, 'product_list.html', context={'product': object_list,'category_list':category_list})






def Categories_Product(request,name):
    catgory = get_object_or_404(Category,name=name)
    products = catgory.products.all()


    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    available = request.GET.get('available')


    if min_price and max_price:
        products = products.filter(price__lte=max_price, price__gte=min_price).distinct()
    if available:
        products = products.filter(available=True)

    page_number = request.GET.get('page')
    paginator = Paginator(products, 2)
    object_list = paginator.get_page(page_number)




    if request.GET.get('sort') == 'newest':
        products_page = paginator.get_page(page_number)
        sorted_products = sorted(products_page,reverse=True, key=lambda p: p.created_at)

        return render(request, 'category_product_list.html', context={'product': sorted_products,'name':name})

    if request.GET.get('sort') == 'visit':
        products_page = paginator.get_page(page_number)
        sorted_products = sorted(products_page,reverse=True, key=lambda p: p.views)
        return render(request, 'category_product_list.html', context={'product': sorted_products,'name':name})

    if request.GET.get('sort') == 'discounts':
       products_page = paginator.get_page(page_number)
       sorted_products = sorted(products_page,reverse=True, key=lambda p: p.discount_percent)
       return render(request, 'category_product_list.html', context={'product': sorted_products,'name':name})

    if request.GET.get('sort') == 'Inexpensive':
        products_page = paginator.get_page(page_number)
        sorted_products = sorted(products_page, key=lambda p: p.price)
        return render(request, 'category_product_list.html', context={'product': sorted_products,'name':name})

    return render(request,'category_product_list.html',{'product':object_list,'name':name})





def Brands_Product(request,name):
    mark = get_object_or_404(Mark,name=name)
    products = mark.products.all()


    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    available = request.GET.get('available')


    if min_price and max_price:
        products = products.filter(price__lte=max_price, price__gte=min_price).distinct()
    if available:
        products = products.filter(available=True)

    page_number = request.GET.get('page')
    paginator = Paginator(products, 2)
    object_list = paginator.get_page(page_number)




    if request.GET.get('sort') == 'newest':
        products_page = paginator.get_page(page_number)
        sorted_products = sorted(products_page,reverse=True, key=lambda p: p.created_at)

        return render(request, 'brands_product_list.html', context={'product': sorted_products,'name':name})

    if request.GET.get('sort') == 'visit':
        products_page = paginator.get_page(page_number)
        sorted_products = sorted(products_page,reverse=True, key=lambda p: p.views)
        return render(request, 'brands_product_list.html', context={'product': sorted_products,'name':name})

    if request.GET.get('sort') == 'discounts':
       products_page = paginator.get_page(page_number)
       sorted_products = sorted(products_page,reverse=True, key=lambda p: p.discount_percent)
       return render(request, 'brands_product_list.html', context={'product': sorted_products,'name':name})

    if request.GET.get('sort') == 'Inexpensive':
        products_page = paginator.get_page(page_number)
        sorted_products = sorted(products_page, key=lambda p: p.price)
        return render(request, 'brands_product_list.html', context={'product': sorted_products,'name':name})

    return render(request,'brands_product_list.html',{'product':object_list,'name':name})




class TreeView(TemplateView):
    template_name = 'tree.html'


class SearchView(View):
    def get(self,request):
        search = request.GET.get('s')
        if search:
            products = Products.objects.filter(
                Q(title__icontains=search) | Q(description__icontains=search) | Q(tag__name__icontains=search) | Q(
                    mark__name__icontains=search) | Q(short_title__icontains=search) | Q(
                    short_description__icontains=search)
                ).distinct()

            page_number = request.GET.get('page')
            paginator = Paginator(products, 2)
            object_list = paginator.get_page(page_number)

            return render(request,'product_search.html',{'product':object_list})
        
        return render(request, 'product_search.html', {'product': {}})


















