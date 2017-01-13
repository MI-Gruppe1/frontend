'''
Created on 05.03.2016

@author: jones
'''



from django.core.management.base import BaseCommand, CommandError
from dashboard.models import BikeStation
from dashboard import services_api
import json

                   
class Command(BaseCommand):


    
    def handle(self, *args, **options):
        with open('andi.json') as data_file:    
			stations = json.load(data_file)
			for s in stations:
				station, created = BikeStation.objects.get_or_create(name=s['name'], location_lat=s['latitude'], location_lon=s['longitude']);
				if created:
					station.save()
        
       
          
        