'''
Created on 19.12.2016

@author: jones
'''
import requests
import time
from time import mktime
import datetime
from pprint import pprint
import urllib
import json
from models import BikeStation
#BESTANDSERVICE

bestand_port = 5000
route_port = 7000
weather_port = 4568
prediction_port = 3000
srdb_port = 6000


def bestand_getall():    
    cmd = 'bestand'
    url = 'http://localhost:'+str(bestand_port)+'/' + cmd
    post = {}
    response = requests.get(url)
    print(url)
    print(response)
    rj = response.json()

    return rj

def bestand_get(name):    
  
	cmd = 'bestand'
	url = 'http://localhost:'+str(bestand_port)+'/' + cmd + '/' + name
	post = {}
	response = requests.get(url)
	rj = response.json()
	pprint(rj)
	return rj
def bestand_getPrediction(names):    
	
	cmd = 'bestandUndVorhersage'
	url = 'http://localhost:'+str(bestand_port)+'/' + cmd
	stationen = names
	

	response = requests.post(url, json=stationen)
	print(response.content)
	formated = "["+response.content+"]"
	print(formated)
	rj = json.loads(formated)
	pprint(rj)
	return rj
#PREDICTION

def prediction_predict(name):

	cmd = 'predictionService'
	print(name)
	url = 'http://localhost:'+str(prediction_port)+'/' + cmd  + '?' + urllib.urlencode({"name" : unicode(name).encode('utf-8')})
	response = requests.get(url)
	print(url)
	pprint(response)
	rj = response.json()
	pprint(rj)
	return rj


#ROUTE


def route_getdirections(start, destination):
	cmd = 'routing'
	post = {'origin' : start,
			'destination' : destination}
	url = 'http://localhost:'+str(route_port)+'/' + cmd + '?' + urllib.urlencode(post)
	pprint(url)
	response = requests.get(url)
	pprint(response)
	if response.status_code != 200:
		print("error")
		pprint(response)
	rj = response.json()
	pprint(rj)
	return response

#STADTRADDB
def srdb_getall(): 

    cmd = 'allStations'
    url = 'http://localhost:'+str(srdb_port)+'/' + cmd

    response = requests.get(url)
    if response.status_code != 200:
        print(url)
        print("error")
        pprint(response)
    rj = response.json()

    return rj

#WEATHER
def srdb_freebikes(name):

    cmd = 'freeBikesOfStation'
    args = {'station_name' : unicode(name).encode('utf-8')}
    url = 'http://localhost:'+str(srdb_port)+'/' + cmd + '?' + urllib.urlencode(args)
    post = {'name' : name }
    print(url)
    response = requests.get(url)
    rj = response.json()

    return rj 
def srdb_freebikesattime(name,timestamp ):


    cmd = 'freeBikesofStationAtSpecTime'
    args = {'station_name' :  unicode(name).encode('utf-8'),
				'information_timestamp' : int(timestamp)}
    url = 'http://localhost:'+str(srdb_port)+'/' + cmd+ '?' + urllib.urlencode(args)
    print(url)
    post = {'name' : name,
            'information_timestamp' : timestamp}
    response = requests.get(url)
    print(response)
    rj = response.json()

    return rj 
def srdb_nextStations(number,latitude,longitude  ):
      
    cmd = 'nextXStationsofLatLong'
    args = {'number_of_stations' : number,
            'latitude' : latitude,
            'longitude' : longitude}
    url = 'http://localhost:'+str(srdb_port)+'/' + cmd + '?' + urllib.urlencode(args) 
    print(url)
    response = requests.get(url)
    pprint(response)
    rj = response.json()
    pprint(rj)

    return rj 
def weather_tempattime(time, lon, lat):

    cmd = 'temperatureAtTime'
    url = 'http://172.17.0.1:'+str(weather_port)+'/' + cmd + '/' 
    post = {'time' : time,
            'lon' : lon,
            'lat' : lat}
    response = requests.post(url, json=post)
    print(repsonse)
    rj = response.json()

    return rj 
def weather_condtime(time, lon, lat):
  
    cmd = 'WeatherConditionAtTime'
    url = 'http://172.17.0.1:'+str(weather_port)+'/' + cmd + '/' 
    post = {'time' : time,
            'lon' : lon,
            'lat' : lat}
    response = requests.post(url, json=post)
    print(response)
    rj = response.json()

    return rj 
def weather_weatherattime(time, lon, lat):
    
    cmd = 'weatherAtTime'
    args = {'time' : time,
            'lon' : lon,
            'lat' : lat}
    url = 'http://172.17.0.1:'+str(weather_port)+'/' + cmd + '?' + urllib.urlencode(args)
    
    print(url)
    response = requests.get(url)
    print(response)

    rj = response.json()

    return rj 
def test_service_api():   
  
    print('SRDB GETALL')
   
    now = datetime.datetime.now()
    lat = "53.55657502"
    lon = "10.02336144"
    start = "Berliner Tor"
    end = "Jungfernstieg"
    names = []
    stations = srdb_getall()
    j = 0
    for s in stations:
        j=j+1
        print(j)
        print("Name: " + s['name'])
        print("Lat: " + str(s['latitude']))
        print("Lon: " + str(s['longitude']))
        print('SRDB FREEBIKES')
        free = srdb_freebikes(s['name'])
        print("free Bikes: " + str(free))
        print('SRDB FREEBIKESATTIME')
	
        for i in range(1, 5):      
        
            dtime = now-datetime.timedelta(hours=i)  
            unixtime = mktime(dtime.timetuple())
            free = srdb_freebikesattime(s['name'], (unixtime))
            print(str(free) + " free bikes . " + str(i) + " hours ago");
        if j == 3:
            break
    print('SRDB NEXTSTATIONS') 
    stations2 = srdb_nextStations(10,lat,lon);

    print("next 10 stations:")
    for s in stations2:
        names.append(s['name'])
        print("Name: " + s['name'])
        print("Lat: " + str(s['latitude']))
        print("Lon: " + str(s['longitude']))
    
  
    print('WEATHER TEMPATTIME')        
    for i in range(1, 5):              
            dtime = now-datetime.timedelta(hours=i)  
            unixtime = mktime(dtime.timetuple())
            weather = weather_weatherattime(int(unixtime), lon, lat)
            pprint(weather);
            print(str(i) + " hours ago");

def test_weather_api():     
	print('WEATHER TEMPATTIME')        
	now = datetime.datetime.now()
	lat = "53.55657502"
	lon = "10.02336144"
	for i in range(1, 5):              
		dtime = now-datetime.timedelta(hours=i)  
		unixtime = mktime(dtime.timetuple())
		weather = weather_weatherattime(int(unixtime), lon, lat)
		pprint(weather);
		print(str(i) + " hours ago");
	
def weather_get_last_hours():     
	print('WEATHER TEMPATTIME')        
	now = datetime.datetime.now()
	lat = "53.55657502"
	lon = "10.02336144"
	for i in range(1, 5):              
            dtime = now-datetime.timedelta(hours=i)  
            unixtime = mktime(dtime.timetuple())
            weather = weather_weatherattime(int(unixtime), lon, lat)
            pprint(weather);
            print(str(i) + " hours ago");
def route_test_route():
	d1 = "53.55657502, 10.02336144"
	d2 = "54.55657502, 10.02336144"
	route_getdirections("Jungfernstieg", "Berliner Tor")


def bestand_test_service():
	print('BESTAND_GETALL') 
	stations3 = bestand_getall()
	names = []
	for s in stations3:
		print("Name: " + s['name'])
		if 'bikes' in s:
			print("Bestand: " + str(s['bikes']))
	print('BESTAND_GET') 
	for s in stations3[:3]:
		bestand = bestand_get(s['name'])
		print("Name: " + bestand['name'])
		print("Bestand: " + str(bestand))
		names.append(s)
	print('BESTAND_GETPREDICTION')

	stations4 = bestand_getPrediction(names)
	for s in stations4:
		pprint(s)
		
def prediction_test():
	stations = BikeStation.objects.all()
	for station in stations[:10]:
		prediction_predict(station.name)
def test_raddb_api():
    print('SRDB GETALL')
   
    now = datetime.datetime.now()
    lat = "53.55657502"
    lon = "10.02336144"
    start = "Berliner Tor"
    end = "Jungfernstieg"
    names = []
    stations = srdb_getall()
    j = 0
    for s in stations:
        j=j+1
        print(j)
        print("Name: " + s['name'])
        print("Lat: " + str(s['latitude']))
        print("Lon: " + str(s['longitude']))
        print('SRDB FREEBIKES')
        free = srdb_freebikes(s['name'])
        print("free Bikes: " + str(free))
        print('SRDB FREEBIKESATTIME')
	
        for i in range(1, 5):      
        
            dtime = now-datetime.timedelta(hours=i)  
            unixtime = mktime(dtime.timetuple())
            free = srdb_freebikesattime(s['name'], (unixtime))
            print(str(free) + " free bikes . " + str(i) + " hours ago");
        if j == 3:
            break
    print('SRDB NEXTSTATIONS') 
    stations2 = srdb_nextStations(10,lat,lon);

    print("next 10 stations:")
    for s in stations2:
        names.append(s['name'])
        print("Name: " + s['name'])
        print("Lat: " + str(s['latitude']))
        print("Lon: " + str(s['longitude']))
		
	
def services_test_all_apis():
	print("Testing SRDB...")
	i = raw_input("Press Enter to continue...")
	test_raddb_api()
	print("\nTesting BestandService...")
	raw_input("Press Enter to continue...")
	bestand_test_service()
	print("\nTesting PredictionService...")
	raw_input("Press Enter to continue...")
	prediction_test()
	print("\nTesting WeatherService...")
	raw_input("Press Enter to continue...")
	test_weather_api()
	print("\nTesting RouteService...")
	raw_input("Press Enter to continue...")
	route_test_route();
	