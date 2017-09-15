from django.conf.urls import url
from django.shortcuts import render,redirect
from cmdb import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^host/', views.host),
    url(r'^host_ajax/', views.host_ajax),
    url(r'^app/', views.app),
    url(r'^addapp/', views.addapp),
    url(r'^editapp/', views.editapp),
    url(r'^user_list/',views.user_list),
    url(r'^login/',views.login),
    url(r'^showdtl/',views.showdtl),

]
