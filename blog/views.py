from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from blog.models import Blog ,BlogComment


class BlogListView(ListView):
    template_name = 'blog_list.html'
    model = Blog
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context





class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'

    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj

    def post(self, request, *args, **kwargs):
        blog = self.get_object()
        body = request.POST.get('body')
        user = request.user
        parent_id = request.POST.get('parent_id')
        if parent_id == 0 or not parent_id:
            messages.success(request, f'نظر شما با موفقیت ایجاد شد', extra_tags='alert alert-success')
        else:
            comment = BlogComment.objects.get(id=parent_id)
            messages.success(request, f'نظر شما در جواب به کاربر {comment.user.username} با موفقیت ایجاد شد',extra_tags='alert alert-success')

        BlogComment.objects.create(blog=blog,user=user,body=body,parent_id=parent_id)
        return redirect('blog:detail_blogs',blog.slug)

