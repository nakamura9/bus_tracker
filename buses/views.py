# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os 
import json
import urllib
from django.contrib import messages
from . import forms
from . import serializers
from . import models
from django.urls import reverse_lazy
from common.utilities import ExtraContext
from rest_framework.viewsets import ModelViewSet




from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView

CREATE_TEMPLATE = os.path.join('common', 'create_template.html')

class POSView(TemplateView):
    template_name = os.path.join('buses', 'POS.html')

class BusTrackerAdminDashBoard(TemplateView):
    template_name = os.path.join('buses', 'dashboard.html')

    def get(self, request, *args, **kwargs):
        messages.info(request, 'Logged in successfully. Welcome, %s' % request.user.username)
        return super().get(request, *args, **kwargs)

class BusScheduleView(TemplateView):
    template_name = os.path.join('buses', 'schedule.html')


class CreateTripView(CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.TripForm
    success_url = reverse_lazy('buses:dashboard')
    extra_context = {
        'title': 'Create New Trip'
    }


class CreateRouteCheckPointView(CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.RouteCheckpointForm
    success_url = reverse_lazy('buses:dashboard')
    extra_context = {
        'title': 'Create New Route Checkpoint'
    }


class CreateRouteView(CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.RouteForm
    success_url = reverse_lazy('buses:dashboard')
    extra_context = {
        'title': 'Create New Route'
    }


class CreateBusView(CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.BusForm
    success_url = reverse_lazy('buses:dashboard')
    extra_context = {
        'title': 'Add Bus to Tracker'
    }

class CreateBusCompanyView(CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.BusCompanyForm
    success_url = reverse_lazy('buses:dashboard')
    extra_context = {
        'title': 'Register A new Bus Company'
    }


class CreateScheduleView(CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.ScheduleForm
    success_url = reverse_lazy('buses:dashboard')
    extra_context = {
        'title': 'Add A New Bus Schedule'
    }


class BusDetailView():
    pass


class BusListView():
    pass

class TripAPIView(ModelViewSet):
    serializer_class = serializers.TripSerializer
    queryset = models.Trip.objects.all()