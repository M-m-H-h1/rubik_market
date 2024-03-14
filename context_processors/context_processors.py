from django.contrib.auth.models import User
from cart.cart_module import Cart
from products.models import Products, GroupCategory , CategoryTitles , Category , Mark
from blog.models import Blog


def group_categories(request):
    group_categories = GroupCategory.objects.all()
    category_titles = CategoryTitles.objects.all()
    categories = Category.objects.all()
    products = Products.objects.all()
    user = User.objects.all()
    marks = Mark.objects.all()
    blog = Blog.objects.all()
    item_count = 5
    categories_has_pro = Category.objects.filter(products__isnull=False).distinct()


    return {'group_categories':group_categories,'caregory_titles':category_titles,'categories':categories,'products':products,'users':user,'marks':marks,'blogs':blog,'cart_count':item_count,'cat_product':categories_has_pro}


