from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, vehicle_id):
    return HttpResponse("You're looking at vehicle %s." % vehicle_id)

def results(request, vehicle_id):
    return HttpResponse("You're looking at the results of poll %s." % vehicle_id)

def vote(request, vehicle_id):
    return HttpResponse("You're voting on poll %s." % vehicle_id)
