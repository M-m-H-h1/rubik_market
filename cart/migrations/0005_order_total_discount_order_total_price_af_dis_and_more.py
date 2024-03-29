# Generated by Django 4.2.7 on 2024-02-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_orderitem_final_price_alter_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_discount',
            field=models.CharField(blank=True, default=0, max_length=100, null=True, verbose_name='جمع تخفیف'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price_af_dis',
            field=models.CharField(blank=True, default=0, max_length=100, null=True, verbose_name='قیمت نهایی بعد از تخفیف'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.CharField(default=0, max_length=100, verbose_name='قیمت قبل از تخفیف'),
        ),
    ]
