# Generated by Django 4.2.7 on 2024-02-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_remove_message_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='اسم کاربر'),
        ),
    ]
