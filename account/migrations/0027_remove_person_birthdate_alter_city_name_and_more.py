# Generated by Django 4.2.7 on 2024-02-29 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_city_country_alter_address_ostan_person_city_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='birthdate',
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.city'),
        ),
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.country'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=124),
        ),
    ]
