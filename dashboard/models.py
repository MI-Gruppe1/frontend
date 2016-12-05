from django.db import models
class WeatherStation(models.Model):
    wid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    location_lat = models.FloatField(default=0)
    location_lon = models.FloatField(default=0)

class BikeStation(models.Model): 
    name = models.CharField(max_length=200)
    location_lat = models.FloatField(default=0)
    location_lon = models.FloatField(default=0)
    slots = models.IntegerField(default=0)
    def __str__(self):
        return u'{0}: {1}'.format(self.name, str(self.slots))
class BikeStationData(models.Model):
    station = models.ForeignKey(BikeStation, related_name='dataset')
    used = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published', auto_now=True)
    def __str__(self):
        return u'{0}: {1}'.format(self.station, str(self.used))
    
    
class MicroService(models.Model): 
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
   
    def __str__(self):
        return u'{0}: {1}'.format(self.name, str(self.status))
class MicroServiceLogEntry(models.Model):
    service = models.ForeignKey(MicroService, related_name='dataset')
    code = models.IntegerField(default=0)
    desc = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True)
    def __str__(self):
        return u'{0}: {1} - {2}'.format(self.service, str(self.code), str(self.desc))