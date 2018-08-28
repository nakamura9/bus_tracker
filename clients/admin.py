# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

admin.site.register(models.Client)
admin.site.register(models.TrackingTicket)
admin.site.register(models.TicketAlertRecepients)