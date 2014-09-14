import requests
import json

from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from locations.models import Vehicle, Stop, Route

class IndexView(generic.ListView):
    template_name = 'locations/index.html'
    context_object_name = 'latest_vehicle_list'

    def get_queryset(self):
        """Return the last five vehicles."""
        return Vehicle.objects.filter(
            seconds_since_report__lte=30,
            seconds_since_report__gt=0
        ).order_by('-seconds_since_report')[:5]


class DetailView(generic.DetailView):
    model = Vehicle
    template_name = 'locations/detail.html'

    def get_queryset(self):
        """
        Exclude any vehicles with nonsensical seconds_since_report
        """
        return Vehicle.objects.filter(seconds_since_report__gt=0)


class ResultsView(generic.DetailView):
    model = Vehicle
    template_name = 'locations/results.html'


class StopsView(generic.ListView):
    model = Stop


class RoutesView(generic.ListView):
    model = Route


def stopRoutes(request, stop_id):
    stop = get_object_or_404(Stop, stop_id=stop_id)
    routes = stop.routes.all()
    return render(request, 'locations/route_list.html', {'route_list': routes})       


def routeVehicles(request, route_id):
    # route_id = models.CharField(max_length=50)
    vehicles = get_list_or_404(Vehicle, route_id=route_id)
    # route = get_object_or_404(Route, stop_id=route_id)
    # vehicles = route.vehicles.all()
    return render(request, 'locations/vehicle_list.html', {'vehicle_list': vehicles})


def vote(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    vehicle.votes += 1
    vehicle.save()
    return HttpResponseRedirect(reverse('locations:results', args=(vehicle.id,)))


def pull(request, route_id):
    r = requests.get('http://api.metro.net/agencies/lametro/routes/%s/vehicles/' % (route_id))
    data = json.loads(r.text)
    for item in data['items']:
        # print item
        if 'run_id' not in item:
            item['run_id'] = None
        vehicle = Vehicle(
            seconds_since_report=item['seconds_since_report'],
            run_id=item['run_id'],
            longitude=item['longitude'],
            heading=item['heading'],
            route_id=item['route_id'],
            predictable=item['predictable'],
            latitude=item['latitude'],
            vehicle_id=item['id']
        )
        vehicle.save()
    return HttpResponseRedirect(reverse('locations:routes'))