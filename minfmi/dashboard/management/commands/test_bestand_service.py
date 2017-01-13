'''
Created on 05.03.2016

@author: jones
'''



from django.core.management.base import BaseCommand, CommandError
from dashboard.models import BikeStation
from dashboard import services_api


                   
class Command(BaseCommand):

    
    def handle(self, *args, **options):
        services_api.bestand_test_service()
        
       
          
        