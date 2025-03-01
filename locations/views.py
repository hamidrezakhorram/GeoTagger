from django.shortcuts import render ,redirect
from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer
from django.views.generic.base import TemplateView
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.http import JsonResponse
from .forms import LocationForm
import csv
from django.http import HttpResponse
import json
class LocationView(viewsets.ModelViewSet):
    queryset =Location.objects.all()
    serializer_class = LocationSerializer

class MapView(TemplateView):
    template_name = "locations\map.html"

def search_nearby(request):
    try:
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        radius = request.GET.get('radius', 10)  # Default to 10 km

        if lat is None or lon is None:
            return JsonResponse({'error': 'Latitude and longitude are required'}, status=400)

        lat = float(lat)
        lon = float(lon)
        radius = float(radius)

        user_location = Point(lon, lat, srid=4326)
        locations = Location.objects.annotate(distance=Distance('coordinates', user_location))
        locations = locations.filter(distance__lte=radius * 1000).order_by('distance')

        data = [
            {'name': loc.name, 'description': loc.description, 'distance_km': loc.distance.km}
            for loc in locations
        ]

        return JsonResponse(data, safe=False)
    
    except ValueError:
        return JsonResponse({'error': 'Invalid latitude, longitude, or radius'}, status=400)

def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('locations:map')
    else:
        form = LocationForm()
    return render(request, 'locations/add_location.html', {'form': form})

def export_locations(request, format):
    locations = Location.objects.all().values('name', 'description', 'coordinates')

    if format == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="locations.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Description', 'Coordinates'])
        for loc in locations:
            writer.writerow([loc['name'], loc['description'], loc['coordinates']])
        return response
    elif format == 'json':
        response = HttpResponse(json.dumps(list(locations)), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="locations.json"'
        return response

