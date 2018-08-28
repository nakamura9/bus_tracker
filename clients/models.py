# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Client(models.Model):
    client_id = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    @property
    def trips(self):
        return TrackingTicket.objects.filter(client=self)

    def __str__(self):
        return self.client_id

class TrackingTicket(models.Model):
    FEATURE_LEVELS = [
        (1, 'Basic'),
        (2, 'Enhanced'),
        (3, 'Ultimate')
    ]
    #enhanced and ultimate get more alerts via sms 
    # as well as access to the tracking site 
    # basic is only for sms alerts in 3 locations 
    trip = models.ForeignKey('buses.Trip', on_delete=None)
    client = models.ForeignKey('clients.Client', on_delete=None)
    one_time_password = models.CharField(max_length=32)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    feature_level = models.PositiveSmallIntegerField(choices = FEATURE_LEVELS)

    def __str__(self):
        return str(self.client)

    #the other phone numbers enhanced and ultimate users can access

class TicketAlertRecepients(models.Model):
    ticket = models.ForeignKey('clients.TrackingTicket', on_delete=None)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.phone_number