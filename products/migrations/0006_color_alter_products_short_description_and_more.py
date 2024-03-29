# Generated by Django 4.2.7 on 2024-01-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_description_products_short_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20, verbose_name='رنگ')),
                ('f_color', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='short_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='توضیحات کوتاه'),
        ),
        migrations.AlterField(
            model_name='products',
            name='short_title',
            field=models.CharField(blank=True, help_text='<h3 style="color: #0a58ca" class="help">این فیلد باید در حد  یک جمله کوچک از ویژگی محصول باشد<h3>', max_length=100, null=True, verbose_name='عنوان مختصر'),
        ),
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, help_text='<h3 style="color: #0a58ca" class="help">ادرس بر اساس فیلد (عنوان مختصر) ساخته میشود<h3>', null=True, unique=True, verbose_name='آدرس'),
        ),
    ]
