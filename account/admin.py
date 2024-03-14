from django.contrib import admin

from account import models

admin.site.register(models.Profile)
admin.site.register(models.ContactUs)
admin.site.register(models.Message)
admin.site.register(models.Code_Password_Recovery)
admin.site.register(models.Address)
admin.site.register(models.City)

class CitiesItemAdmin(admin.TabularInline):
    model = models.City


@admin.register(models.State)
class OrderAdmin(admin.ModelAdmin):
    inlines = (CitiesItemAdmin,)



@admin.register(models.Us_Team)
class UsTeamAdmin(admin.ModelAdmin):
    readonly_fields = ('email',)
