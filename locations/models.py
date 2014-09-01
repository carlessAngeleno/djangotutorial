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


    def __unicode__(self):
        return self.vehicle_id

    def was_reported_recently(self):
        return self.seconds_since_report < 30

    was_reported_recently.admin_order_field = 'seconds_since_report'
    was_reported_recently.boolean = True
    was_reported_recently.short_description = 'Predictable?'
