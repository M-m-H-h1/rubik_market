from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField

from products.models import Tag


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/blog', verbose_name='عکس مقاله')
    tag = models.ManyToManyField(Tag, verbose_name='تگ')
    short_body = models.TextField(max_length=400, verbose_name='بدنه کوچک شده', null=True, blank=True)
    body = RichTextField(null=True, blank=True,verbose_name='بدنه')
    slug = models.SlugField(unique=True, verbose_name='آدرس', allow_unicode=True, null=True, blank=True)
    views = models.IntegerField(default=0, verbose_name='امار بازدید')
    created = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    updated = jmodels.jDateTimeField(auto_now=True)

    def show_create_time(self):
        return self.created.strftime("ارسال شده در %d %B %Y در ساعت %H:%M")

    def get_absolute_url(self):
        return reverse('blog:detail_blogs', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='مقاله', related_name='blog_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments', verbose_name="کاربر")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="در پاسخ به",related_name='blog_replies')
    body = models.TextField(verbose_name="متن کامنت")
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.body} - ( {self.blog.title} )'

    class Meta:
        verbose_name = 'کامنت (مقاله)'
        verbose_name_plural = "کامنت ها (مقالات)"

    def show_create_time(self):
        return self.created_at.strftime("ارسال شده در %d %B %Y در ساعت %H:%M")
