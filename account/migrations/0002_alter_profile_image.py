# Generated by Django 4.2.7 on 2024-01-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/profile_user.png', upload_to='images/account/profile', verbose_name='عکس پروفایل'),
        ),
    ]