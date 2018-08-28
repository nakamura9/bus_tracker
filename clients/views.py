# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json 
import urllib3

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from . import forms
from . import models
from django.utils import timezone
from django.contrib import messages


CREATE_TEMPLATE = os.path.join('common', 'create_template.html')

class ClientLogin(FormView):
    form_class = forms.ClientPortalForm
    template_name = os.path.join('clients', 'login.html')
    
    def post(self, request, *args, **kwargs):
        NOW = timezone.now()
        try:
            ticket = models.TrackingTicket.objects.get(
                one_time_password= request.POST['one_time_password'])
            if NOW > ticket.valid_from:
                if NOW < ticket.valid_to:
                    return HttpResponseRedirect(reverse_lazy(
                        'clients:dashboard', kwargs={
                    'pk': ticket.pk
                }))
                else:
                    ticket.delete()
                    messages.error(request, 'The ticket used has expired')
                    return HttpResponseRedirect(reverse_lazy(request.path))
            else: return HttpResponseRedirect(reverse_lazy(request.path))
        except:
            messages.error(request, 'The password you entered is invalid.')
            return HttpResponseRedirect(request.path)
        

class ClientDashBoard(DetailView):
    model = models.TrackingTicket
    template_name = os.path.join('clients', 'dashboard.html')

