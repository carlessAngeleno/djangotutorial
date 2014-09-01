from django.db import models

# Create your models here.
class Vehicle(models.Model):
    seconds_since_report = models.IntegerField()
    run_id = models.CharField(max_length=50)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    heading = models.DecimalField(max_digits=4, decimal_places=1)
    route_id = models.CharField(max_length=50)
    predictable = models.BooleanField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    vehicle_id = models.CharField(max_length=50)