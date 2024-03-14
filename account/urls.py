from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register', views.RgisterUserView.as_view(), name='register_user'),
    path('login', views.login_user, name='login_user'),
    path('logout', views.user_logout, name='logout_user'),
    path('contactus', views.ContactUsView.as_view(), name='contactus'),
    path('message', views.MessageView.as_view(), name='message'),
    path('add-address', views.AddAddressView.as_view(), name='add_address'),
    path('password-recovery', views.Password_Recovery.as_view(), name='password_recovery'),
    path('verify-code', views.VerifyCodeView.as_view(), name='verify-code'),
    path('forget_password', views.Forget_Password.as_view(), name='forget_password'),
    path('change_password', views.ChangePasswordView.as_view(), name='change_password'),
    path('profile', views.EditProfileUser.as_view(), name='profile_user'),
    path("delete-profile-image/", views.DeleteUserImage.as_view(), name="delete_image"),
    path("delete-address/<int:pk>", views.DeleteAddressView.as_view(), name="delete_address"),
    path("edit-address/<int:pk>", views.AddressUpdateView.as_view(), name="edit_address"),
    path('ajax/Load-cities/', views.Load_Cities, name='Ajax_load_cities'),
    path('factors/', views.UserFactorsView.as_view(), name='user_factors'),
    path('factor-delete/<int:pk>', views.DeleteFactorView.as_view(), name='factor_delete'),
    path('load/', views.load_more, name='load'),
    path('fav-add/<int:pk>', views.AddFavoriteProduct.as_view(), name='fav_add'),
    path('favorite-product', views.FavoriteProductDetailView.as_view(), name='fav_detail'),
    path('fav-delete/<str:id>', views.FavDeleteView.as_view(), name='fav_delete'),
]
