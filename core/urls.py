from django.urls import path
from . import views

urlpatterns = [
    path('cities/', views.city_list, name='city-list'),
    path('weather/<str:city_name>/', views.weather, name='weather'),
]
