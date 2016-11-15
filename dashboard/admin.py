from django.contrib import admin
from dashboard.models import BikeStation, BikeStationData, MicroService, MicroServiceLogEntry
# Register your models here.


admin.site.register(BikeStation)
admin.site.register(BikeStationData)
admin.site.register(MicroService)
admin.site.register(MicroServiceLogEntry)