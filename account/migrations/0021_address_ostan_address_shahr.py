# Generated by Django 4.2.7 on 2024-02-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_code_password_recovery_expired_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='ostan',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='address',
            name='shahr',
            field=models.CharField(default='', max_length=20),
        ),
    ]
