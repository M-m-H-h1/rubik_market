# Generated by Django 4.2.7 on 2024-02-16 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_message_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
    ]
