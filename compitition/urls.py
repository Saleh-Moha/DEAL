from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . views import *
app_name = 'Comptition'
urlpatterns = [
    path('',Questions_list,name='questions'),
    path('<str:slug>',Answer_question,name='answer'),
]