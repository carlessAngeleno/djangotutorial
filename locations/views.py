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
        return Vehicle.objects.order_by('-seconds_since_report')[:5]


class DetailView(generic.DetailView):
    model = Vehicle
    template_name = 'locations/detail.html'


class ResultsView(generic.DetailView):
    model = Vehicle
    template_name = 'locations/results.html'


# def index(request):
#     latest_vehicle_list = Vehicle.objects.order_by('-seconds_since_report')[:5]
#     context = {'latest_vehicle_list': latest_vehicle_list}
#     return render(request, 'locations/index.html', context)


# def detail(request, vehicle_id):
#     vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
#     return render(request, 'locations/detail.html', {'vehicle': vehicle})


# def results(request, vehicle_id):
#     vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
#     return render(request, 'locations/results.html', {'vehicle': vehicle})


def vote(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    vehicle.votes += 1
    vehicle.save()
    return HttpResponseRedirect(reverse('locations:results', args=(vehicle.id,)))