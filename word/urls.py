from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import wordPost

urlpatterns = [
    path('', wordPost, name='word'),
]