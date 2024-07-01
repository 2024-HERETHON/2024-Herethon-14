from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import generate_and_save_poem

app_name='poem'
urlpatterns = [
    path('', generate_and_save_poem, name='generate_poem'),
]