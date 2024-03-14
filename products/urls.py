from django.urls import path,re_path,include
from . import views

app_name = 'product'

urlpatterns=[
    path('special-product/<int:id>',views.delete_Special_Sale,name='delete_specila_pro'),
    re_path(r'detail/(?P<slug>[-\w]+)',views.ProductDetailView.as_view(),name='detail_product'),
    path('list/',views.Product_List,name='list_product'),
    path('cat-product/<str:name>',views.Categories_Product,name='cat_products'),
    path('brands-products/<str:name>',views.Brands_Product,name='brands_products'),
    path('tree', views.TreeView.as_view(), name='TreeView'),
    path('search', views.SearchView.as_view(), name='search'),


]



