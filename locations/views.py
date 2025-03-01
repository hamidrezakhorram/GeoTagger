from django.shortcuts import render
from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer

class LocationView(viewsets.ModelViewSet):
    queryset =Location.objects.all()
    serializer_class = LocationSerializer
    