from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('detail',views.CartDetailView.as_view(),name='detail'),
    path('add/<int:pk>',views.CartAddView.as_view(),name='cart_add'),
    path('delete/<str:id>',views.CartDeleteView.as_view(),name='cart_delete'),
    path('order/<int:pk>',views.OrderDetailView.as_view(),name='order_detail'),
    path('order/add',views.OrderCreationView.as_view(),name='order_creation'),
    path('success-pey',views.SuccessPeyView.as_view(),name='success_pey'),
    path('apply-discount-code/<int:pk>',views.ApplyDiscountView.as_view(),name='apply_discount'),

]