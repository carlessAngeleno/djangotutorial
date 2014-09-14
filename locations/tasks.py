from __future__ import absolute_import
import requests
import json

from celery import shared_task
from time import sleep

from locations.models import Vehicle

@shared_task
def add(x, y):
    sleep(2)
    return x - y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def pull_data(route_id):
    r = requests.get('http://api.metro.net/agencies/lametro/routes/%s/vehicles/' % (route_id))
    data = json.loads(r.text)
    for item in data['items']:
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