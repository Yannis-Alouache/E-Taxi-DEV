from django.db import models
# Create your models here.

class Reservation(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)
    phone = models.CharField(blank=False, null=False, max_length=10)
    date = models.CharField(blank=False, null=False, max_length=24)
    addressDeparture = models.CharField(blank=False, null=False, max_length=300)
    addressArrival = models.CharField(blank=False, null=False, max_length=300)

    def __str__(self):
        return f'Réservation ' + self.name 
    


