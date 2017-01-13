'''
Created on 05.03.2016

@author: jones
'''



from django.core.management.base import BaseCommand, CommandError
from dashboard.models import BikeStation
from dashboard import services_api
from pprint import pprint

                   
class Command(BaseCommand):
	
	def handle(self, *args, **options):
		stations = services_api.bestand_getall()  
		for s in stations:
			station, created = BikeStation.objects.get_or_create(name=s["name"])
			
			if created:
				station.location_lat=s["latitude"]
				station.location_lon=s["longitude"]
			if "bikes" in s:
				station.bikes=s["bikes"]
				prediction = services_api.bestand_getPrediction([s])
				station.prediction = prediction[0]['prediction']
			print(station.name)
			print(station.location_lat)
			print(station.location_lon)
			print(station.bikes)
			station.save()