from django.urls import path
from . import views

urlpatterns = [
    path('api/cities/', views.city_list, name='city-list'),
    path('api/weather/<str:city_name>/', views.weather, name='weather'),
]
