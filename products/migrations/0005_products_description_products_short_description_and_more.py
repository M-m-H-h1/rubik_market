# Generated by Django 4.2.7 on 2024-01-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_images_options_remove_special_sale_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AddField(
            model_name='products',
            name='short_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='توضیحات'),
        ),
        migrations.AddField(
            model_name='products',
            name='short_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان مختصر'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ساخت'),
        ),
        migrations.AlterField(
            model_name='products',
            name='images',
            field=models.ManyToManyField(related_name='products', to='products.images', verbose_name='تصاویر'),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(max_length=300, verbose_name='عنوان'),
        ),
    ]
