from django.db import models

# Create your models here.

class GeoData(models.Model):
    ip = models.GenericIPAddressField(max_length=100, primary_key=True)
    url = models.URLField(max_length=50, blank=True)
    continent_code = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)
    region_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_eu = models.BooleanField(default=True)