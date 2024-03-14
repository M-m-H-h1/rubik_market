# Generated by Django 4.2.7 on 2024-02-15 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0008_alter_contactus_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Us_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'اضافه کردن کاربر به تیم ما',
                'verbose_name_plural': 'اضافه کردن کاربران به تیم ما',
            },
        ),
    ]
