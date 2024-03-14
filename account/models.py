from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from products import help_texts


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='image')
    image = models.ImageField(upload_to='images/account/profile', default='images/account/profile_user.png',
                              verbose_name='عکس پروفایل')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'


class ContactUs(models.Model):
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.description[:50]

    class Meta:
        verbose_name = 'توضیحات صفحه درباره'
        verbose_name_plural = 'توضیحات های صفحه درباره ما'


class Us_Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    instagram_id = models.URLField(verbose_name='آدرس اینستاگرام', null=True, blank=True)
    telegram_id = models.URLField(verbose_name='آدرس تلگرام', null=True, blank=True)
    email = models.EmailField(verbose_name='ایمیل', null=True, blank=True, editable=False,
                              help_text=help_texts.edit_email)

    def save(self, *args, **kwargs):
        self.email = self.user.email
        super(Us_Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'اضافه کردن کاربر به بخش تیم ما'
        verbose_name_plural = 'اضافه کردن کاربران به بخش تیم ما'


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', null=True, blank=True)
    name = models.CharField(verbose_name='اسم کاربر', max_length=100, null=True, blank=True)
    email = models.EmailField(verbose_name='ایمیل', null=True, blank=True)
    subject = models.CharField(max_length=200, verbose_name='موضوع پیام', null=True, blank=True)
    body = models.TextField(verbose_name='متن پیام')

    def __str__(self):
        return f'{self.name} - {self.body[:50]}'

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class Code_Password_Recovery(models.Model):
    code = models.IntegerField(max_length=5, verbose_name='کد')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    expiration_time = models.TimeField(null=True, blank=True, verbose_name='تاریخ انقضا')
    expired = models.BooleanField(default=True, verbose_name='ایا این کد قابل استفاده هست ؟')

    def __str__(self):
        return f'{self.code} - {self.email}'

    class Meta:
        verbose_name = 'کد بخش فراموشی رمز'
        verbose_name_plural = 'کد های بخش فراموشی رمز'


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name='کاربر')
    fullname = models.CharField(max_length=40, verbose_name='نام و نام خانوادگی گیرنده ')
    phone = models.CharField(max_length=12, verbose_name='تلفن فرد گیرنده')
    state = models.ForeignKey('State',null=True,blank=True,on_delete=models.PROTECT, default='', verbose_name='استان')
    city = models.ForeignKey('City',null=True,blank=True,on_delete=models.PROTECT, default='', verbose_name='شهر')
    email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    default = models.BooleanField(default=False,verbose_name='آدرس پیشفرض')
    address = models.TextField(verbose_name='آدرس')

    def __str__(self):
        return f'{self.user.username}- ( {self.address[:50]} ) '

    class Meta:
        verbose_name = 'ادرس تحویل محصول'
        verbose_name_plural = 'ادرس های تحویل محصولات'



class State(models.Model):
    name = models.CharField(null=True,blank=True,max_length=40,verbose_name='نام استان')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'


class City(models.Model):
    state = models.ForeignKey(State,null=True,blank=True, on_delete=models.CASCADE,verbose_name='استان والد')
    name = models.CharField(null=True,blank=True,max_length=40,verbose_name='نام شهر')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'
