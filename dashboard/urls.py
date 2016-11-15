from django.conf.urls import url

from .views import views

urlpatterns = [
    url(r'^dash/$', views.dash, name='welcome'),
    url(r'^dash/dash$', views.dash, name='dash'),
    url(r'^dash/maps', views.maps, name='maps'),
    url(r'^dash/graphs$', views.graphs, name='graphs'),
    url(r'^dash/about$', views.index, name='about'),
    url(r'^dash/services$', views.services, name='services'),    
    url(r'^dash/services/log$', views.servicelog, name='servicelog'),
]