# Generated by Django 4.2.7 on 2024-01-02 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_color_f_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'رنگ', 'verbose_name_plural': 'رنگ ها'},
        ),
        migrations.AddField(
            model_name='color',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.products', verbose_name='محصول'),
        ),
    ]
