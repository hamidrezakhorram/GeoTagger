from django import forms
from .models import Location
from django.contrib.gis.geos import Point

class LocationForm(forms.ModelForm):
    latitude = forms.FloatField(label="Latitude")
    longitude = forms.FloatField(label="Longitude")

    class Meta:
        model = Location
        fields = ["name", "description", "latitude", "longitude"]  # Explicitly add latitude & longitude

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.coordinates = Point(self.cleaned_data["longitude"], self.cleaned_data["latitude"])  # Store as a Point
        if commit:
            instance.save()
        return instance  
        