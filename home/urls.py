from django.contrib import admin
from django.urls import path,include
from . views import *
app_name = 'Home'
urlpatterns = [
    # path('',openingone),
    path('',openingone,name='home'),
]