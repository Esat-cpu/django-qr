from django.urls import path
from . import views

app_name = "olustur"
urlpatterns = [
    path('', views.home, name='home'),
    path('/<int:pk>/', views.home_with_form, name="home_with_form"),
]
