# Generated by Django 4.2.7 on 2024-02-27 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0019_code_password_recovery_expiration_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code_password_recovery',
            name='expired',
            field=models.BooleanField(default=True, verbose_name='ایا این کد قابل استفاده هست ؟'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=12, verbose_name='تلفن')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'ادرس تحویل محصول',
                'verbose_name_plural': 'ادرس های تحویل محصولات',
            },
        ),
    ]
