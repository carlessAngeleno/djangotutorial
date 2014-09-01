from django.contrib import admin
from locations.models import Vehicle

# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    fields = [
        'run_id', 
        'vehicle_id', 
        'route_id', 
        'heading',
        'seconds_since_report',
        'latitude',
        'longitude',
        'predictable'
    ]

admin.site.register(Vehicle, VehicleAdmin)
