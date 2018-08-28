from django import forms 
from common.forms import BootstrapMixin
from . import models 

class TripForm(forms.ModelForm, BootstrapMixin):
    class Meta:
        model = models.Trip
        fields = '__all__'


class BusCompanyForm(forms.ModelForm, BootstrapMixin):
    class Meta:
        model = models.BusCompany
        fields = '__all__'


class BusForm(forms.ModelForm, BootstrapMixin):
    class Meta:
        model = models.Bus
        fields = '__all__'


class RouteForm(forms.ModelForm, BootstrapMixin):
    class Meta:
        model = models.Route
        fields = '__all__'


class RouteCheckpointForm(forms.ModelForm, BootstrapMixin):
    class Meta:
        model = models.RouteCheckPoint
        fields = '__all__'


class ScheduleForm(forms.ModelForm, BootstrapMixin):
    class Meta:
        model = models.BusSchedule
        fields = '__all__'