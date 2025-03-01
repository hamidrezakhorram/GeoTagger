from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()

    def get_coordinates(self, obj):
        if obj.coordinates:  # Ensure coordinates exist
            return [obj.coordinates.x, obj.coordinates.y]  # [longitude, latitude]
        return None  # If missing, return None
    class Meta:
        model = Location
        fields = ("id", "name", "description","coordinates")
       # geo_field = "coordinates"
