from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('',views.HomeProductsView.as_view(), name='main'),
    path('fag', views.FrequentlyAskedQuestionsView.as_view(), name='fag'),

]
