from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from dashboard.models import WeatherStation, BikeStation, BikeStationData, MicroService,MicroServiceLogEntry
from dashboard import services_api
from pprint import pprint
from dashboard.templatetags import template_extras
import time
from time import mktime
from datetime import datetime, timedelta
def route(request):
	pprint(request.POST)
	route = ""
	try: 
		station = BikeStation.objects.get(name=(request.POST["origin"]));
		origin = str(station.location_lat) + ","  + str(station.location_lon)
	except:
		origin = request.POST["origin"];
	try: 
		station = BikeStation.objects.get(name=(request.POST["destination"]));
		destination = str(station.location_lat) + "," + str(station.location_lon)
	except:
		destination = request.POST["destination"]

	route = services_api.route_getdirections(origin, destination)			
	
	
	return HttpResponse(route, content_type="application/json")
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
	labels = []
	verlauf = []
	bikes = 0
	if request.POST["station"]:
			try:
				station = BikeStation.objects.get(id=int(request.POST["station"]));
			except:
				station = BikeStation.objects.get(name=(request.POST["station"]));
			
			#bs = services_api.bestand_get(station.name)
			ps = services_api.bestand_getPrediction([{'name' : station.name}])
			if len(ps) > 0:
				bikes = ps[0]['bikes']
				prediction = ps[0]['prediction']
				verlauf = ps[0]['history']
				verlauf.append(bikes)
				#verlauf.append(prediction)
			else:
			
				prediction = station.prediction
				
				now = datetime.now()
				for i in range(0, 5):         
					dtime = now-timedelta(hours=i)  
					unixtime = mktime(dtime.timetuple())
					free = services_api.srdb_freebikesattime(station.name, (unixtime))
					verlauf.append(free)
				
			station.bikes = verlauf[0]
			bikes = station.bikes
			
			now = datetime.now()
			for i in range(0, 5):              
				dtime = now-timedelta(hours=i)  
				labels.append((dtime+timedelta(hours=1)).strftime('%H:%M'))
			labels.reverse()
			verlauf.reverse()
	else:
		station = BikeStation.objects.first()
		
	context = {
			"station" : station,
			"bikes" : bikes,
			"verlauf" : verlauf,
			"labels" : labels,
			"prediction" : template_extras.formatPrediction(int(bikes), int(prediction))
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


def station(request, mid):
	
	print(mid)
	station = BikeStation.objects.get(id=int(mid));
	
	
		
	context = getContext(station)
	return render(request, 'station.html', context)

def wstation(request, mid):
    try:
        station =    WeatherStation.objects.get(id=id);
    except:
        station = WeatherStation.objects.first()
    
   
    context = {'station' : station,
               }
    return render(request, 'wstation.html', context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def getContext(station):    
 	now = datetime.now()

	lat = station.location_lat
	lon = station.location_lon
	temperatur = []
	luftdruck = []
	luftfeuchte = []
	windgeschwindigkeit = []   
	labels = []
	verlauf = []
	print('WEATHER TEMPATTIME')        

	for i in range(0, 6):              
			dtime = now-timedelta(hours=i)  
			labels.append((dtime+timedelta(hours=1)).strftime('%H:%M'))
			unixtime = mktime(dtime.timetuple())
			weather = services_api.weather_weatherattime(int(unixtime), lon, lat)
			pprint(weather);
			print(str(i) + " hours ago");
			temperatur.append(weather['temperature'])
			luftdruck.append(weather['pressure'])
			luftfeuchte.append(weather['humidity'])
			windgeschwindigkeit.append(weather['windSpeed'])
			wetterDesc = weather['weatherDesc']; 
			wetterDescDetail = weather['weatherDescDetail']; 
			wetterStationName = weather['stationName']; 
			wetterIcon = weather['weatherIcon']; 
	
	temperatur.reverse()
	luftdruck.reverse()
	luftfeuchte.reverse()
	windgeschwindigkeit.reverse()
	labels.reverse()
	
	context = {
			"labels" : labels,  
			"lat" : lat,
			"lon" : lon,
			"station" : station,
			"temperatur": temperatur,
			"luftdruck" : luftdruck,
			"luftfeuchte" : luftfeuchte,
			"windgeschwindigkeit" : windgeschwindigkeit,
			"wetterDesc" : wetterDesc,
			"wetterDescDetail" : wetterDescDetail,
			"wetterStationname" : wetterStationName,
			"wetterIcon" : wetterIcon,
			};
	return context
def dash(request):
    
	now = datetime.now()

	lat = "53.55657502"
	lon = "10.02336144"
	temperatur = []
	luftdruck = []
	luftfeuchte = []
	windgeschwindigkeit = []   
	labels = []
	print('WEATHER TEMPATTIME')        
	print('BESTAND_GETALL') 
	stations3 = services_api.bestand_getall()
	names = []
	for s in stations3:
		print("Name: " + s['name'])
	
		if 'bikes' in s:
			try:
				bs = BikeStation.objects.get(name=s['name'])
				bs.bikes = int(s['bikes'])
				bs.save();
				print("Bestand: " + str(s['bikes']))
			except:
				pass
	for i in range(0, 6):              
			dtime = now-timedelta(hours=i)  
			labels.append((dtime+timedelta(hours=1)).strftime('%H:%M'))
			unixtime = mktime(dtime.timetuple())
			weather = services_api.weather_weatherattime(int(unixtime), lon, lat)
			pprint(weather);
			print(str(i) + " hours ago");
			temperatur.append(weather['temperature'])
			luftdruck.append(weather['pressure'])
			luftfeuchte.append(weather['humidity'])
			windgeschwindigkeit.append(weather['windSpeed'])
			wetterDesc = weather['weatherDesc']; 
			wetterDescDetail = weather['weatherDescDetail']; 
			wetterStationName = weather['stationName']; 
	
	temperatur.reverse()
	luftdruck.reverse()
	luftfeuchte.reverse()
	windgeschwindigkeit.reverse()
	labels.reverse()
	stationen = BikeStation.objects.all()
	context = {
			"labels" : labels,  
			"lat" : lat,
			"lon" : lon,
			"stationen" : stationen,
			"temperatur": temperatur,
			"luftdruck" : luftdruck,
			"luftfeuchte" : luftfeuchte,
			"windgeschwindigkeit" : windgeschwindigkeit,
			"wetterDesc" : wetterDesc,
			"wetterDescDetail" : wetterDescDetail,
			"wetterStationname" : wetterStationName,
			};
	return render(request, 'dash.html', context)
