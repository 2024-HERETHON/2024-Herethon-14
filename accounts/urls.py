from django.contrib import admin
from django.urls import path
from django.urls import path, include
from accounts.views import signup, login, logout, setting
from django.conf import settings
from django.conf.urls.static import static

app_name='accounts'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name= 'logout'),
    path('setting/', setting, name='setting'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)