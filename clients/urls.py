from django.urls import path
from . import views 

app_name = "clients"

urlpatterns = [
    path('login/', views.ClientLogin.as_view(), name='login'),
    path('dashboard/<int:pk>', views.ClientLogin.as_view(), name='dashboard')
]