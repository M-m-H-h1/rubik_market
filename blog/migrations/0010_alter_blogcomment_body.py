# Generated by Django 4.2.7 on 2024-03-11 14:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blogcomment_blog_alter_blogcomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='متن کامنت'),
        ),
    ]