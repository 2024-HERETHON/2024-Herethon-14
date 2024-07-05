from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import wordPost, learn_word, word_detail,voca



app_name='word'
urlpatterns = [
    path('', learn_word, name='learn_word'),
    path('detail/<str:word>/', word_detail, name='word_detail'),
    path('voca/', voca, name='voca'),
]