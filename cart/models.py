from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django_jalali.db import models as jmodels
from jalali_date import datetime2jalali
from persiantools import jdatetime

from products.models import Products, Color, Memory


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders',verbose_name="کاربر")
    total_price = models.CharField(max_length=100,default=0,verbose_name='قیمت قبل از تخفیف')
    total_price_af_dis = models.CharField(null=True,blank=True,max_length=100,default=0,verbose_name='قیمت نهایی بعد از تخفیف')
    total_discount = models.CharField(null=True,blank=True,max_length=100,default=0,verbose_name='جمع تخفیف')
    total_discount_code = models.IntegerField(null=True,blank=True,default=0,verbose_name='جمع تخفیف کد تخفیف')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ساخته شده")
    is_paid = models.BooleanField(default=False,verbose_name='ایا پرداخت شده است ؟')

    class Meta:
        verbose_name = 'سفارش کاربر'
        verbose_name_plural = 'سفارش های کاربران'

    def __str__(self):
        return self.user.username

    def get_jalali_date_for_show(self):
        if self.created_at:
            jalali_date = datetime2jalali(self.created_at)
            formatted_date = jalali_date.strftime("در %d %B %Y ساعت %H:%M")
            return formatted_date
        else:
            return format_html('<p style="color: #fa2c2c">ندارد<p>')


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items',verbose_name='سفارش')
    product = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='items',verbose_name='محصول')
    color = models.ForeignKey(Color,on_delete=models.CASCADE,verbose_name='رنگ',null=True,blank=True)
    memory = models.ForeignKey(Memory,on_delete=models.CASCADE,verbose_name='حافظه',null=True,blank=True)
    quantity = models.SmallIntegerField(verbose_name='تعداد')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    final_price = models.PositiveIntegerField(default=0,verbose_name='قیمت نهایی')
    created_at = jmodels.jDateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        verbose_name = 'محصولات سفارش کاربر'
        verbose_name_plural = 'محصولات های سفارش کاربر'


    def __str__(self):
        return self.product.short_title





class DiscountCode(models.Model):
    name = models.CharField(max_length=20,unique=True,verbose_name='شناسه کد تخفیف')
    discount = models.SmallIntegerField(default=0,verbose_name='درصد تخفیف')
    quantity = models.SmallIntegerField(default=1,verbose_name='تعداد باقیمانده معتبر')


    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'

    def __str__(self):
        return self.name
