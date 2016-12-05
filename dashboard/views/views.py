from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from dashboard.models import WeatherStation, BikeStation, BikeStationData, MicroService,MicroServiceLogEntry
from rest_framework import viewsets
from dashboard.serializers import MicroServiceSerializer, MicroServiceLogEntrySerializer, BikeStationSerializer, BikeStationDataSerializer
from pprint import pprint

def index(request):
    context = {}
    return render(request, 'welcome.html', context)
def about(request):
    dataset1 = BikeStationData.objects.filter(station=BikeStation.objects.first()).order_by("-pub_date").values_list("used", flat=True)
    dataset2 = BikeStationData.objects.filter(station=BikeStation.objects.last()).order_by("-pub_date").values_list("used", flat=True)
    print(dataset1)
    print(dataset2)
    context = {
               "xlabels" : [1,2,3,4,5],
               "label1" : BikeStation.objects.first().name,
               "label2" : BikeStation.objects.last().name,
               "data1" : dataset1,
               "data2" : dataset2,
               
               }
    return render(request, 'about.html', context)
def stationen(request):
    stationen = BikeStation.objects.all()
    wstationen = WeatherStation.objects.all()
    context = {
            "stationen" : stationen,
            "wstationen" : wstationen,
            };
    return render(request, 'stationen.html', context)
def station_details(request):
    pprint(request.POST)
    if request.POST["station"]:
        try:
            station = BikeStation.objects.get(id=int(request.POST["station"]));
            dataset1 = BikeStationData.objects.filter(station=station).order_by("-pub_date").values_list("used", flat=True)
            pprint(dataset1)
        except:
            station = BikeStation.objects.first()
    else:
        station = BikeStation.objects.first()
        
    context = {
            "station" : station,
            "dataset" : dataset1
            };
    return render(request, 'station_details.html', context)
def wstation_details(request):
    pprint(request.POST)
    if request.POST["station"]:
        try:
            station = WeatherStation.objects.get(id=int(request.POST["station"]));
           
        except:
            station = WeatherStation.objects.first()
    else:
        station = WeatherStation.objects.first()
        
    context = {
            "station" : station,
            };
    return render(request, 'wstation_details.html', context)

def statistiken(request):
    context = {}
    return render(request, 'statistiken.html', context)
def station(request, mid):
    try:
        station =    BikeStation.objects.get(id=id);
        wstation =    WeatherStation.objects.first();
    except:
        station = BikeStation.objects.first()
        wstation =    WeatherStation.objects.first();
    
    dataset1 = BikeStationData.objects.filter(station=station).order_by("-pub_date").values_list("used", flat=True)
  
    context = {'station' : station,
               'wstation' : wstation,
               'stationsdata' : dataset1,
               }
    return render(request, 'station.html', context)

def wstation(request, mid):
    try:
        station =    WeatherStation.objects.get(id=id);
    except:
        station = WeatherStation.objects.first()
    
   
    context = {'station' : station,
               }
    return render(request, 'wstation.html', context)

def maps(request):
    context = {}
    return render(request, 'maps.html', context)

def graphs(request):
    context = {}
    return render(request, 'graphs.html', context)

def dash(request):
    stationen = BikeStation.objects.all()
    wstationen = WeatherStation.objects.all()
    context = {
            "stationen" : stationen,
            "wstationen" : wstationen,
            };
    return render(request, 'dash.html', context)

def services(request):
    
    context = {"services" : MicroService.objects.all()}
    return render(request, 'services.html', context)

def servicelog(request):
    context = {"entries" : MicroServiceLogEntry.objects.all().order_by("-pub_date")}
    return render(request, 'servicelog.html', context)

class BikeStationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BikeStation.objects.all()
    serializer_class = BikeStationSerializer


class BikeStationDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = BikeStationData.objects.all()
    serializer_class = BikeStationDataSerializer
    
class MicroServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MicroService.objects.all()
    serializer_class = MicroServiceSerializer


class MicroServiceLogEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = MicroServiceLogEntry.objects.all()
    serializer_class = MicroServiceLogEntrySerializer