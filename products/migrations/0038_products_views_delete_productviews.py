# Generated by Django 4.2.7 on 2024-02-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_productviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='ProductViews',
        ),
    ]