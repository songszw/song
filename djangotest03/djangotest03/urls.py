
from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^cmdb/', include('app01.urls')),
]
