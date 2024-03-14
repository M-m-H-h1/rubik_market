# Generated by Django 4.2.7 on 2024-01-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_products_memory_alter_color_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory', models.CharField(choices=[('128 گیگ', '128 گیگ'), ('360 گیگ', '360 گیگ')], max_length=50, verbose_name='حافظه')),
            ],
            options={
                'verbose_name': 'رنگ',
                'verbose_name_plural': 'رنگ ها',
            },
        ),
    ]
