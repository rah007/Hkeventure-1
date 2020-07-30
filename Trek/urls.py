# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path

from Trek.views import Home_view, Home

urlpatterns = [
    path("" , Home, name='home')
]  
