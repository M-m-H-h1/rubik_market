# Generated by Django 4.2.7 on 2024-01-31 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hitcount', '0005_alter_blacklistip_id_alter_blacklistuseragent_id_and_more'),
        ('products', '0030_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='views',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hitcount.hitcount'),
        ),
    ]