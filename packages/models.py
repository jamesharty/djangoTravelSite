from django.db import models
from datetime import datetime
from hotels.models import Hotel 


# Create your models here.

# Create your views here.
class Package(models.Model):
    packageName = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    travelIncluded = models.CharField(max_length=200)
    hotelName = models.ForeignKey(Hotel,on_delete=models.DO_NOTHING)
    price = models.IntegerField(default = 0)
    startDate = models.DateField(blank=True)
    endDate = models.DateField(blank=True)
    
    def __str__(self):
        return self.packageName
