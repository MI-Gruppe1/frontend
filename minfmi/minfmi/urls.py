
from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from dashboard.views import views
# Serializers define the API representation.


# Routers provide an easy way of automatically determining the URL conf.


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),  
    url(r'^', include('dashboard.urls')),
]

