"""Hikeventure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Trek.views import form_data, Home_view, test_view

from Trek.views import Home, Treks, Road_Trip, River_Rafting, Contact,About,Details, Book
from Trek.views import nubra,sham,markha,leopard,srinagar,darcha,Tso,zanskar,indus,suru,shey,terms,privacy

admin.site.site_header = "Hikeventure Admin"
admin.site.site_title = "Hikeventure Admin Portal"
admin.site.index_title = "Welcome to Hikeventure Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', form_data),
    # path('Home/', Home_view),
    # path('form-view/', trek_form_view),
    path('test/', test_view),
    path('',     include('Trek.urls')),
    
    path('Home/', Home),
    path('Treks/', Treks),
    path('road_trip/', Road_Trip),
    path('river_rafting/', River_Rafting),
    path('Contact/', Contact),
    path('nubra/', nubra),
    path('sham/', sham),
    path('markha/', markha),
    path('leopard/', leopard),
    path('srinagar/', srinagar),
    path('darcha/', darcha),
    path('Tso/', Tso),
    path('zanskar/', zanskar),
    path('indus/', indus),
    path('suru/', suru),
    path('shey/', shey),
    path('terms/', terms),
    path('privacy/', privacy),
    path('About/', About),
    # path('Details/', Details),
    path('Book/', Book),

    
    
]  