# Generated by Django 4.2.7 on 2024-01-02 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_color_options_color_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='product',
        ),
        migrations.AddField(
            model_name='products',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.color'),
        ),
    ]