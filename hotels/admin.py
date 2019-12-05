from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Hotel

class HotelAdmin(admin.ModelAdmin):
    list_display=('id','hotelName','rating','city','country')
    list_display_links=('id','hotelName')
    search_fields=('id',)
    list_per_page=25

admin.site.register(Hotel,HotelAdmin)