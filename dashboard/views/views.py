from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from dashboard.models import BikeStation, BikeStationData, MicroService,MicroServiceLogEntry
from rest_framework import viewsets
from dashboard.serializers import MicroServiceSerializer, MicroServiceLogEntrySerializer, BikeStationSerializer, BikeStationDataSerializer


def index(request):
    context = {}
    return render(request, 'dash/welcome.html', context)
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
    return render(request, 'dash/about.html', context)

def maps(request):
    context = {}
    return render(request, 'dash/maps.html', context)

def graphs(request):
    context = {}
    return render(request, 'dash/graphs.html', context)

def dash(request):
    context = {"title" : "Dashboard" }
    return render(request, 'dash/dash.html', context)

def services(request):
    
    context = {"services" : MicroService.objects.all()}
    return render(request, 'dash/services.html', context)

def servicelog(request):
    context = {"entries" : MicroServiceLogEntry.objects.all().order_by("-pub_date")}
    return render(request, 'dash/servicelog.html', context)

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