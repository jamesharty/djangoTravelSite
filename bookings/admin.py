from django.contrib import admin

# Register your models here.
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display=('id','customerID','packageName','price', 'startDate','endDate')
    list_display_links=('id',)
    search_fields=('id',)
    list_per_page=25

admin.site.register(Booking,BookingAdmin)