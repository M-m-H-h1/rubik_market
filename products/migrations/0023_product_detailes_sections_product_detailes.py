# Generated by Django 4.2.7 on 2024-01-08 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_alter_products_category_alter_review_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Detailes_Sections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'عناون بخش توضیحات محصول',
                'verbose_name_plural': 'عناون بخش توضیحات محصول ها',
            },
        ),
        migrations.CreateModel(
            name='Product_Detailes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300, verbose_name='سوال')),
                ('answer', models.CharField(max_length=300, verbose_name='جواب')),
                ('product_detailes_sections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product_detailes_sections')),
            ],
            options={
                'verbose_name': 'بخش توضیحات محصول',
                'verbose_name_plural': 'بخش توضیحات محصول ها',
            },
        ),
    ]
