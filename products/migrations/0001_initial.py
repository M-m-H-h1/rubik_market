# Generated by Django 4.2.7 on 2023-12-27 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='عنوان')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('top', models.BooleanField(default=False, verbose_name='برگزیده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='GroupCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/Group_Category', verbose_name='عکس')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'گروه بندی دسته بندی',
                'verbose_name_plural': 'گروه بندی دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='نام')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'مارک',
                'verbose_name_plural': 'مارک ها',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('discount_percent', models.SmallIntegerField(blank=True, null=True, verbose_name='درصد تخفیف')),
                ('Price_after_discount', models.IntegerField(blank=True, null=True, verbose_name='قیمت بعد از تخفیف ')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='آدرس')),
                ('stars', models.SmallIntegerField(blank=True, null=True, verbose_name='ستاره')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, null=True, related_name='products', to='products.category', verbose_name='دسته بندی')),
                ('mark', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.mark', verbose_name='مارک')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='Top_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='محصولات')),
            ],
            options={
                'verbose_name': 'محصول منتخب',
                'verbose_name_plural': 'محصولات منتخب',
            },
        ),
        migrations.CreateModel(
            name='Special_Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='زمان پایان')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(help_text=' <h3 style="color: #0a58ca">توجه داشته باشید باید محصولی که انتخاب میکنید دارای درصد تخفیف باشه<h3>', on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='محصولات')),
            ],
            options={
                'verbose_name': 'محصول ویژه',
                'verbose_name_plural': 'محصولات ویژه',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/products', verbose_name='عکس محصول')),
                ('product', models.ManyToManyField(related_name='image', to='products.products', verbose_name='محصولات')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='عنوان')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categorygroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categorytitles', to='products.groupcategory', verbose_name='گروه')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'سر فصل دسته بندی ها',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ManyToManyField(blank=True, null=True, related_name='tilte_cat', to='products.categorytitles', verbose_name='والد'),
        ),
    ]