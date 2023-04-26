from django.urls import path
from .views import index, get_countries, get_cities

urlpatterns = [
    path('d/', index, name='index'),
    path('get_countries/', get_countries, name='get_countries'),
    path('get_cities/', get_cities, name='get_cities'),
]
