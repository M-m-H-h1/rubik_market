# Generated by Django 4.2.7 on 2024-02-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_us_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='us_team',
            options={'verbose_name': 'اضافه کردن کاربر به بخش تیم ما', 'verbose_name_plural': 'اضافه کردن کاربران به بخش تیم ما'},
        ),
        migrations.AddField(
            model_name='us_team',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل'),
        ),
        migrations.AddField(
            model_name='us_team',
            name='instagram_id',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس اینستاگرام'),
        ),
        migrations.AddField(
            model_name='us_team',
            name='telegram_id',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس تلگرام'),
        ),
    ]
