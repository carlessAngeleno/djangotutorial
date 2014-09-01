from django.contrib import admin
from locations.models import Vehicle

# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Vehicle', {'fields': ['run_id', 'vehicle_id', 'route_id']}),
        (
            'Status',  
            {
                'fields': [
                    'seconds_since_report', 
                    'latitude', 
                    'longitude',
                    'heading'
                ]
            }
        ),
        ('Other', {'fields': ['predictable']})
    ]

admin.site.register(Vehicle, VehicleAdmin)
