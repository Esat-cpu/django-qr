from django.urls import path
from . import views

app_name = "olustur"
urlpatterns = [
    path('', views.home, name= 'home'),
]
