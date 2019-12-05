from django.contrib import admin

# Register your models here.
from .models import Package

class PackageAdmin(admin.ModelAdmin):
    list_display=('id','packageName','type','country','price', 'startDate','endDate')
    list_display_links=('id','packageName')
    search_fields=('id',)
    list_per_page=25

admin.site.register(Package,PackageAdmin)