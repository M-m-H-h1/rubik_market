# Generated by Django 4.2.7 on 2024-01-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(related_name='products', to='products.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='review',
            name='description',
            field=models.TextField(help_text='<h3 style="color: #0a58ca" class="help">برای نظم بیشتر متن  کلی رو به صورت پاراگراف به پاراگراف درون فیلد های توضیحات به تعداد دلخواه وارد کنید<h3>', verbose_name='توضیحات'),
        ),
    ]
