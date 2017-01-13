from django.conf.urls import url

from .views import views

urlpatterns = [
    url(r'^$', views.dash, name='dash'),
    url(r'^dash/$', views.dash, name='dash'),
    
    url(r'^station/(?P<mid>\d+)', views.station, name='station'),
    url(r'^wstation/(?P<mid>\d)', views.wstation, name='wstation'),
    url(r'^stationdetails/', views.station_details, name='stationdetails'),
    url(r'^wstationdetails/', views.wstation_details, name='wstationdetails'),
    url(r'^stationen/', views.stationen, name='stationen'),
    url(r'^route/', views.route, name='route'),

]