from django.contrib import admin
from locations.models import Vehicle, Stop, Route

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

    list_display = ('run_id', 'vehicle_id', 'route_id', 'was_reported_recently')

    list_filter = ['vehicle_id', 'route_id']
    search_fields = ['vehicle_id']


class StopAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Stop', {'fields': ['stop_id', 'display_name']}),
        ('Location', {'fields': ['latitude', 'longitude']})
    ]

    list_display = ('stop_id', 'display_name', 'latitude', 'longitude')

    list_filter = ['latitude', 'longitude']
    search_fields = ['display_name']


class RouteAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Route', {'fields': ['route_id', 'display_name']})
    ]

    list_display = ('route_id', 'display_name')

    search_fields = ['display_name']


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Stop, StopAdmin)
admin.site.register(Route, RouteAdmin)
