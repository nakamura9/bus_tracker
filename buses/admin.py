# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models


admin.site.register(models.BusCompany)
admin.site.register(models.BusSchedule)
admin.site.register(models.Trip)
admin.site.register(models.Bus)
admin.site.register(models.Route)
admin.site.register(models.RouteCheckPoint)