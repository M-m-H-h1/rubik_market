from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from products import models
from django import forms

admin.site.register(models.GroupCategory)
admin.site.register(models.Top_Product)
admin.site.register(models.Mark)
admin.site.register(models.Memory)
admin.site.register(models.Product_Detailes_Sections)
admin.site.register(models.Product_Detailes)
admin.site.register(models.Comment)
admin.site.register(models.Tag)







class MyModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('product','get_jalali_date_for_show')




admin.site.register(models.Special_Sale,MyModelAdmin)
#
@admin.register(models.Category)
class CategoryAdminMain(admin.ModelAdmin):
    list_display = ('name', 'get_parents','top')
    list_editable = ('top',)
    list_filter = ('top',)


    @admin.display(description='دسته بندی والد')
    def get_parents(self, obj):
        return [product.name for product in obj.parent.all()]

class ReviewsInline(admin.StackedInline):
    model = models.Review


class ProductsAdminForm(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'color' in self.fields:
            self.fields['color'].choices = [(c.id, c.get_color_display()) for c in models.Color.objects.all()]


class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = ('title', 'get_categories','get_color_display','get_tags')
    prepopulated_fields = {'slug': ['short_title']}
    list_filter = ('discount_percent', 'created_at')
    search_fields = ('title', 'category__name')
    inlines = (ReviewsInline,)




    @admin.display(description='دسته بندی ها')
    def get_categories(self, obj):
        return [category.name for category in obj.category.all()]

    @admin.display(description='تگ ها')
    def get_tags(self, obj):
        return [tag.name for tag in obj.tag.all()]

    @admin.display(description='رنگ')
    def get_color_display(self, obj):
        return [color.get_color_display() for color in obj.color.all()]


admin.site.register(models.Products, ProductsAdmin)




@admin.register(models.CategoryTitles)
class CategoryTitleAdmin(admin.ModelAdmin):
    list_display = ('name','categorygroup')

class ProductInline(admin.TabularInline):
    model = models.Products.images.through

@admin.register(models.Images)
class ProductAdminMain(admin.ModelAdmin):
    list_display = ('show_image','id')
    inlines = (ProductInline,)


@admin.register(models.Color)
class ProductAdminMain(admin.ModelAdmin):
    exclude = ('f_color',)
    list_display = ('color','f_color')

@admin.register(models.Review)
class ProductAdminMain(admin.ModelAdmin):
    list_display = ('__str__','product')

