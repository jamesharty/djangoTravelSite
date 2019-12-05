from django.contrib import admin

# Register your models here.

from .models import Profile

class accountsAdmin(admin.ModelAdmin):
    list_display=('id','user','firstName','lastName','cardNumber')
    list_display_links=('id','user','firstName')
    search_fields=('id',)
    list_per_page=25

admin.site.register(Profile,accountsAdmin)