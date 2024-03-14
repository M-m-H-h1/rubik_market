# Generated by Django 4.2.7 on 2023-12-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_images_product_products_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'عکس', 'verbose_name_plural': 'عکس ها'},
        ),
        migrations.RemoveField(
            model_name='special_sale',
            name='created_at',
        ),
        migrations.AddField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ManyToManyField(related_name='tilte_cat', to='products.categorytitles', verbose_name='والد'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='images/products', verbose_name='عکس'),
        ),
    ]
