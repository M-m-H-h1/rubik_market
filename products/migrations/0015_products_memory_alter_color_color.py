# Generated by Django 4.2.7 on 2024-01-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_products_color_products_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='memory',
            field=models.CharField(blank=True, choices=[('128 گیگ', '128 گیگ'), ('360 گیگ', '360 گیگ')], max_length=150, null=True, verbose_name='حافظه'),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(choices=[('red', 'قرمز'), ('black', 'مشکی'), ('blue', 'آبی'), ('grey', 'خاکستری'), ('white', 'سفید')], max_length=20, verbose_name='رنگ'),
        ),
    ]
