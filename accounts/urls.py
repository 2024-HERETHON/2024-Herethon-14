from django.contrib import admin
from django.urls import path
from django.urls import path, include
from accounts.views import signup, login, logout

app_name='accounts'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name= 'logout'),
]