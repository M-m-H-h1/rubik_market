# Generated by Django 4.2.7 on 2024-01-02 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_color_product_products_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(choices=[('red', 'قرمز'), ('green', 'مشکی'), ('blue', 'آبی'), ('gray', 'خاکستری')], max_length=20, verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.color'),
        ),
    ]
