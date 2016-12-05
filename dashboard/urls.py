from django.conf.urls import url

from .views import views

urlpatterns = [
    url(r'^$', views.index, name='welcome'),
    url(r'^dash/$', views.dash, name='dash'),
    url(r'^maps', views.maps, name='maps'),
    url(r'^graphs$', views.graphs, name='graphs'),
    url(r'^station/(?P<mid>\d)', views.station, name='station'),
    url(r'^wstation/(?P<mid>\d)', views.wstation, name='wstation'),
    url(r'^stationdetails/', views.station_details, name='stationdetails'),
    url(r'^wstationdetails/', views.wstation_details, name='wstationdetails'),
    url(r'^stationen/', views.stationen, name='stationen'),
    url(r'^statistiken', views.statistiken, name='statistiken'),
    url(r'^about$', views.about, name='about'),
    url(r'^services$', views.services, name='services'),    
    url(r'^services/log$', views.servicelog, name='servicelog'),
]