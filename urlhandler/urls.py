from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'^products/$', views.my_view, name='urlname')
]