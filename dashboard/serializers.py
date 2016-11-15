'''
Created on 10.10.2016

@author: jones
'''
from dashboard.models import BikeStation, BikeStationData, MicroService, MicroServiceLogEntry
from rest_framework import serializers


class BikeStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeStation
        fields = ('id', 'name', 'location_lat', 'location_lon', 'slots')


class BikeStationDataSerializer(serializers.ModelSerializer):
    station = serializers.PrimaryKeyRelatedField(queryset=BikeStation.objects.all())
    class Meta:
        model = BikeStationData        
        fields = ('station', 'used')
        
        

class MicroServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroService
        fields = ('id', 'name', 'status', 'desc')


class MicroServiceLogEntrySerializer(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(queryset=MicroService.objects.all())
    class Meta:
        model = MicroServiceLogEntry        
        fields = ('service', 'code', 'desc')
        
        
