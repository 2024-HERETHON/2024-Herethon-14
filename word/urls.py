from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import wordPost, learn_word



app_name='word'
urlpatterns = [
    path('', learn_word, name='learn_word'),
]