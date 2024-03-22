from django.contrib import admin
from django.urls import path,include
from . views import *
app_name = 'Blog'
urlpatterns = [
    path('', blog_list,name='blog'),
    path('/<str:slug>',blog_details,name='blog_detail'),
]
