from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('list', views.BlogListView.as_view(), name='list_blogs'),
    re_path(r'detail/(?P<slug>[-\w]+)', views.BlogDetailView.as_view(), name='detail_blogs'),
]
