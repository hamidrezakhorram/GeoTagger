from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    coordinates = models.PointField(srid=4326)  

    def __str__(self):
        return self.name
