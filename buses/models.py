# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from bus_tracker import settings


class BusCompany(models.Model):
    legal_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True, 
        upload_to=settings.MEDIA_ROOT)

    def __str__(self):
        return self.legal_name

class BusSchedule(models.Model):
    start_period = models.DateField()
    end_period = models.DateField()

    def __str__(self):
        return "%s - %s" %( self.start_period, self.end_period)
    

class Trip(models.Model):
    STATUSES = [
        (0, 'Scheduled'),
        (1, 'Delayed'),
        (2, 'On Time'),
        (3, 'Cancelled'),
        (4, 'En Route'),
        (5, 'Completed'),
    ]
    name = models.CharField(max_length=255, default="")
    description = models.TextField(blank=True, default="")
    schedule =models.ForeignKey('buses.BusSchedule', on_delete=None)
    status = models.PositiveIntegerField(choices = STATUSES)
    # if recurring this is the datum date other trips are scheduled from
    date = models.DateField()
    departure_time = models.TimeField()
    duration = models.DurationField()
    bus = models.ForeignKey('buses.Bus', on_delete=None)
    route = models.ForeignKey('buses.Route', on_delete=None)
    recurring = models.BooleanField(default=False)

    def __str__(self):
        return "%s: %s" % (str(self.bus.company), str(self.bus))
    # for reccuring trips, make sure the save method creates multiple trips for the bus 

class Bus(models.Model):
    company = models.ForeignKey('buses.BusCompany', on_delete=None)
    routes = models.ManyToManyField('buses.Route')
    registration_number = models.CharField(max_length=255)
    tracking_id = models.CharField(max_length=255)

    def __str__(self):
        return self.registration_number

class Route(models.Model):
    name = models.CharField(max_length=255)
    checkpoints = models.ManyToManyField('buses.RouteCheckPoint', null=True, 
        blank=True, related_name='checkpoints')
    destination = models.ForeignKey('buses.RouteCheckPoint', on_delete=None , 
        related_name='destination')
    starting_point = models.ForeignKey('buses.RouteCheckPoint', on_delete=None, 
        related_name = 'point_of_origin')

    def __str__(self):
        return self.name

class RouteCheckPoint(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name