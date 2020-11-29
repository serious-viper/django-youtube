from django.urls import path
from . import views
urlpatterns = [
    path('', views.ytdl , name="ytdl"),
    path('help', views.help , name="help")
    
    
]
