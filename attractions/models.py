from django.db import models
from datetime import datetime


# Create your models here.

# Create your views here.
class Attraction(models.Model):
    ranking = models.IntegerField(default = 0)
    attractionName = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image1 = models.ImageField(upload_to='attractions/photos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.attractionName