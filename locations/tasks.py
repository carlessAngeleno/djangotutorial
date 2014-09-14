from __future__ import absolute_import

from celery import shared_task
from time import sleep


@shared_task
def add(x, y):
    sleep(30)
    for i in range(30):
        l = 3
        print l
    return x - y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)