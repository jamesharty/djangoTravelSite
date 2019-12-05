from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotelName = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    def __str__(self):
        return self.hotelName