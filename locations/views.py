from django.http import HttpResponse
from django.shortcuts import render

from locations.models import Vehicle

# Create your views here.
def index(request):
    latest_vehicle_list = Vehicle.objects.order_by('-seconds_since_report')[:5]
    context = {'latest_vehicle_list': latest_vehicle_list}
    return render(request, 'locations/index.html', context)


def detail(request, vehicle_id):
    return HttpResponse("You're looking at vehicle %s." % vehicle_id)


def results(request, vehicle_id):
    return HttpResponse("You're looking at the results of poll %s." % vehicle_id)


def vote(request, vehicle_id):
    return HttpResponse("You're voting on poll %s." % vehicle_id)