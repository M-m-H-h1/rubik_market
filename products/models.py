import uuid

from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from datetime import datetime
from django_jalali.db import models as jmodels
from account.models import Profile
from star_ratings.models import Rating , AbstractBaseRating
from . import help_texts
from django.utils.html import format_html
from django.urls import reverse
from jalali_date import date2jalali, datetime2jalali
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class GroupCategory(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    image = models.ImageField(upload_to='images/Group_Category',null=True,blank=True,verbose_name='عکس')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'گروه بندی دسته بندی'
        verbose_name_plural = 'گروه بندی دسته بندی ها'


class CategoryTitles(models.Model):
    categorygroup = models.ForeignKey(GroupCategory, on_delete=models.PROTECT, verbose_name='گروه', blank=True,null=True,related_name='categorytitles')
    name = models.CharField(max_length=150, verbose_name='عنوان')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'سر فصل دسته بندی'
        verbose_name_plural = 'سر فصل دسته بندی ها'

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ManyToManyField(CategoryTitles,verbose_name='والد',related_name='tilte_cat',)
    name = models.CharField(max_length=150, verbose_name='عنوان',unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    top = models.BooleanField(default=False,verbose_name='برگزیده')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def get_absolute_url(self):
        return reverse('product:cat_products', kwargs={'name': self.name})

    def __str__(self):
        return self.name

class Mark(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام',unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse('product:brands_products', kwargs={'name': self.name})

    class Meta:
        verbose_name = 'مارک'
        verbose_name_plural = 'مارک ها'

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='images/products',verbose_name='عکس')

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس ها'

    def show_image(self):
        return format_html(f'<img src="{self.image.url}" width="60px" height="50px">')


    show_image.short_description = 'عکس محصول'


    def __str__(self):
        return f'عکس با ایدی {self.id}'


class Products(models.Model):
    comments = GenericRelation('Comment', related_query_name='products')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی',related_name='products')
    mark = models.ForeignKey(Mark, verbose_name='مارک', on_delete=models.SET_NULL, null=True, blank=True,related_name='products')
    tag = models.ManyToManyField('Tag',verbose_name='تگ')
    color = models.ManyToManyField('Color',null=True,blank=True,verbose_name='رنگ')
    images = models.ManyToManyField(Images, verbose_name='تصاویر',related_name='products')
    memory = models.ManyToManyField('Memory',null=True,blank=True,verbose_name='حافظه')
    title = models.CharField(max_length=300,verbose_name='عنوان')
    short_title = models.CharField(max_length=100,verbose_name='عنوان مختصر',null=True,blank=True,help_text=help_texts.product_short_des)
    description = models.TextField(null=True,blank=True,verbose_name='توضیحات')
    short_description = models.CharField(max_length=200,null=True,blank=True,verbose_name='توضیحات کوتاه')
    price = models.IntegerField(verbose_name='قیمت')
    discount_percent = models.SmallIntegerField(verbose_name='درصد تخفیف',null=True,blank=True)
    Price_after_discount = models.IntegerField(verbose_name='قیمت بعد از تخفیف ',null=True,blank=True)
    slug = models.SlugField(unique=True,default=uuid.uuid1,verbose_name='آدرس',allow_unicode=True,null=True,blank=True,help_text=help_texts.product_slug)
    views = models.PositiveIntegerField(default=0,verbose_name='امار بازدید')
    available = models.BooleanField(default=True,verbose_name='کالا موجود است')
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name='تاریخ ساخت')
    updated = models.DateTimeField(auto_now=True)



    def get_absolute_url(self):
        return reverse('product:detail_product', kwargs={'slug': self.slug})


    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def __str__(self):
        return self.title

@receiver(pre_save, sender=Products)
def calculate_price_after_discount(sender, instance, **kwargs):
    if instance.discount_percent:
        instance.Price_after_discount = instance.price - (instance.price * instance.discount_percent // 100)
    if not instance.discount_percent:
        instance.Price_after_discount = None





class Top_Product(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE,verbose_name='محصولات')
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'محصول منتخب'
        verbose_name_plural = 'محصولات منتخب'

    def __str__(self):
        return self.product.title



class Special_Sale (models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE,verbose_name='محصولات',help_text=help_texts.product_ha_time)
    end_time = models.DateTimeField(verbose_name='زمان پایان',null=True,blank=True)


    def get_jalali_date(self):
        if self.end_time:
            jalali_date = datetime2jalali(self.end_time)
            return jalali_date
        else:
            return None

    def get_jalali_date_for_show(self):
        if self.end_time:
            jalali_date = datetime2jalali(self.end_time)
            formatted_date = jalali_date.strftime(' %d %B %Y , ساعت %H:%M:%S')
            return formatted_date
        else:
            return format_html('<p style="color: #fa2c2c">ندارد<p>')

    get_jalali_date_for_show.short_description = 'تاریخ پایان'




    class Meta:
        verbose_name = 'محصول ویژه'
        verbose_name_plural = 'محصولات ویژه'

    def __str__(self):
        return self.product.title

@receiver(pre_save, sender=Special_Sale)
def validate_end_time(sender, instance, **kwargs):
    existing_instance = Special_Sale.objects.exclude(pk=instance.pk).first()
    if existing_instance and existing_instance.end_time is not None and instance.end_time is not None:
        raise ValueError(".شما فقط میتوانید برای یک محصول زمان پایان در نظر بگیرید")




class Color (models.Model):
    # product = models.ForeignKey(Products,on_delete=models.PROTECT,verbose_name= 'محصول',null=True,blank=True)
    color = models.CharField(max_length=20,verbose_name='رنگ',choices=help_texts.COLORS)
    f_color = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'

    def __str__(self):
        return self.color


@receiver(pre_save, sender=Color)
def translate_color_english(sender, instance,*args, **kwargs):


    instance.f_color = instance.color

class Memory(models.Model):
    memory = models.CharField(max_length=50,verbose_name='حافظه',choices=help_texts.Memories)


    class Meta:
        verbose_name = 'حافظه'
        verbose_name_plural = 'حافظه ها'

    def __str__(self):
        return self.memory



class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='محصول',related_name='reviews')
    description = models.TextField(verbose_name='توضیحات',help_text=help_texts.review_description)


    class Meta:
        verbose_name = 'توضیحات'
        verbose_name_plural = 'توضیحات ها'

    def __str__(self):
        return f'{self.description[:80]} ...'



class Product_Detailes_Sections(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='محصول',related_name='product_d_sect')
    title = models.CharField(max_length=250,verbose_name='عنوان')



    class Meta:
        verbose_name = 'عناون بخش توضیحات محصول'
        verbose_name_plural = 'عناون بخش توضیحات محصول ها'

    def __str__(self):
        return self.title



class Product_Detailes(models.Model):
    product_detailes_sections = models.ForeignKey(Product_Detailes_Sections,on_delete=models.CASCADE, verbose_name='عنوان',related_name='product_detail')
    question = models.CharField(max_length=300,verbose_name='سوال')
    answer = models.CharField(max_length=300,verbose_name='جواب')



    class Meta:
        verbose_name = 'بخش توضیحات محصول'
        verbose_name_plural = 'بخش توضیحات محصول ها'

    def __str__(self):
        return f'{self.question} --- {self.answer}'



class Comment(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='محصول',related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="کاربر")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,verbose_name="در پاسخ به", related_name='replies')
    body = models.TextField(verbose_name="متن کامنت")
    created_at = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.body} - ( {self.product.short_title} )'

    class Meta:
        verbose_name = 'کامنت (محصولات)'
        verbose_name_plural = "کامنت ها (محصولات)"

    def show_create_time(self):

        return self.created_at.strftime("ارسال شده در %d %B %Y در ساعت %H:%M")



class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام تگ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = "تگ ها"