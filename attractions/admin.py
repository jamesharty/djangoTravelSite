from django.contrib import admin

# Register your models here.
from .models import Attraction

class AttractionAdmin(admin.ModelAdmin):
    list_display=('id','attractionName','location','country')
    list_display_links=('id','attractionName')
    search_fields=('id',)
    list_per_page=25

admin.site.register(Attraction,AttractionAdmin)