# Generated by Django 4.2.7 on 2024-02-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_alter_address_ostan_alter_address_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=12, verbose_name='تلفن'),
        ),
    ]
