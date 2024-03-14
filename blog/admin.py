from django.contrib import admin
from blog import models



@admin.register(models.Blog)
class BlogsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_filter = ('views', 'created')
    search_fields = ('title', 'body')



@admin.register(models.BlogComment)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('__str__','user')



