from django.conf.urls import url
from django.contrib import admin
from cmdb import views
urlpatterns = [
    url(r'^login', views.login),
    url(r'^index', views.index),
    url(r'^register', views.register),
    url(r'^userlist', views.userlist),
    url(r'^userEdit-(?P<nid>\d+)', views.userEdit),
    url(r'^details-(?P<nid>\d+)', views.details),
    url(r'^delete-(?P<nid>\d+)', views.delete),
]
