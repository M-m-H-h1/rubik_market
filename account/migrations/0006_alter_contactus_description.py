# Generated by Django 4.2.7 on 2024-02-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='description',
            field=models.CharField(max_length=300, verbose_name='توضیحات'),
        ),
    ]
