# Generated by Django 4.2.7 on 2024-03-11 14:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogcomment_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='بدنه'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='body',
            field=models.TextField(verbose_name='متن کامنت'),
        ),
    ]
