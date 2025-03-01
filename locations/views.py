from django.shortcuts import render
from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer
from django.views.generic.base import TemplateView

class LocationView(viewsets.ModelViewSet):
    queryset =Location.objects.all()
    serializer_class = LocationSerializer

class MapView(TemplateView):
    template_name = "locations\map.html"

# def map_view(request):
#      return render(request, 'locations\map.html')