from django.db import models
from datetime import datetime
from accounts.models import Profile


# Create your models here.
class Booking(models.Model):
    customerID = models.IntegerField(default = 0)
    packageName = models.CharField(max_length=200)
    price = models.IntegerField(default = 0)
    startDate = models.DateField( blank=True)
    endDate = models.DateField( blank=True)

    def __str__(self):
        return str(self.id)