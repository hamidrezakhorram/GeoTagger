from django import forms
from .models import Location
from django.contrib.gis.geos import Point

class LocationForm(forms.ModelForm):
    latitude = forms.FloatField(label="Latitude")
    longitude = forms.FloatField(label="Longitude")

    class Meta:
        model = Location
        fields = ["name", "description", "latitude", "longitude"]  

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.coordinates = Point(self.cleaned_data["longitude"], self.cleaned_data["latitude"])  
        if commit:
            instance.save()
        return instance  
        