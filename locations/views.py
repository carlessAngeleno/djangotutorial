from django.shortcuts import render
from django.http import HttpResponse

from locations.models import Vehicle

# Create your views here.
def index(request):
    latest_vehicle_list = Vehicle.objects.order_by('-seconds_since_report')[:5]
    output = ', '.join([v.vehicle_id for v in latest_vehicle_list])
    return HttpResponse(output)

def detail(request, vehicle_id):
    return HttpResponse("You're looking at vehicle %s." % vehicle_id)

def results(request, vehicle_id):
    return HttpResponse("You're looking at the results of poll %s." % vehicle_id)

def vote(request, vehicle_id):
    return HttpResponse("You're voting on poll %s." % vehicle_id)