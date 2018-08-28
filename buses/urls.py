import os 

from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = "buses"
login_path = os.path.join('buses', 'login.html')

urlpatterns = [
    path('dashboard', views.BusTrackerAdminDashBoard.as_view(), name='dashboard'),
    path('create-trip', views.CreateTripView.as_view(), name='create-trip'),
    path('create-bus', views.CreateBusView.as_view(), name='create-bus'),
    path('create-bus-company', views.CreateBusCompanyView.as_view(), name='create-bus-company'),
    path('create-route', views.CreateRouteView.as_view(), name='create-route'),
    path('create-route-checkpoint', views.CreateRouteCheckPointView.as_view(), name='create-route-checkpoint'),
    path('create-schedule', views.CreateScheduleView.as_view(), name='create-schedule'),
    path('login', LoginView.as_view(template_name=login_path), name = 'login')
]