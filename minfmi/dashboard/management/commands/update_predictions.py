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
		stations = BikeStation.objects.all()  
		for station in stations:
			prediction = services_api.bestand_getPrediction([{'name' : station.name}])
			station.prediction = prediction[0]['prediction']
			station.bikes=prediction[0]["bikes"]
			print(station.name)
			print(station.location_lat)
			print(station.location_lon)
			print(station.bikes)
			station.save()