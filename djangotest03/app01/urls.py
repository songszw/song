
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views


urlpatterns = [
    url(r'^index', views.index,name='index'),
    url(r'^login', views.Login.as_view()),
    # url(r'^login', views.login),
    url(r'^register', views.register),
    # url(r'^detail', views.detail),
    url(r'^detail-(?P<nid>\d+).html', views.detail),
]
