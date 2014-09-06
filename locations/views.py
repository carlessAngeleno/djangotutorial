from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from locations.models import Vehicle

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


def vote(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    vehicle.votes += 1
    vehicle.save()
    return HttpResponseRedirect(reverse('locations:results', args=(vehicle.id,)))