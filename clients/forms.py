from django import forms
from common.forms import BootstrapMixin


class ClientPortalForm(BootstrapMixin, forms.Form):
    one_time_password = forms.CharField()