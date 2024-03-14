# Generated by Django 4.2.7 on 2024-02-28 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_orderitem_color_alter_orderitem_memory'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='final_price',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت نهایی'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.CharField(default=0, max_length=100, verbose_name='قیمت نهایی'),
        ),
    ]