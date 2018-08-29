from . import models
from rest_framework.serializers import ModelSerializer

class TripSerializer(ModelSerializer):
    class Meta:
        fields = ['id', 'name']
        model = models.Trip