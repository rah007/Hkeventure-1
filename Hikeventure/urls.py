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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', form_data),
    path('Home/', Home_view),
    # path('form-view/', trek_form_view),
    path('test/', test_view),
    path('',     include('Trek.urls')),
    
    path('Index/', Home),
    path('Treks/', Treks),
    path('road_trip/', Road_Trip),
    path('river_rafting/', River_Rafting),
    path('Contact/', Contact),
    path('About/', About),
    path('Details/', Details),
    path('Book/', Book),
]  