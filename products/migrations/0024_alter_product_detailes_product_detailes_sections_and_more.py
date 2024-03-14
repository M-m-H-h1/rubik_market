# Generated by Django 4.2.7 on 2024-01-08 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_product_detailes_sections_product_detailes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detailes',
            name='product_detailes_sections',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_detail', to='products.product_detailes_sections', verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='product_detailes_sections',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_d_sect', to='products.products', verbose_name='محصول'),
        ),
    ]