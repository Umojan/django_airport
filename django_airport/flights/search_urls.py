from django.urls import path
from .views import search_flights

urlpatterns = [
    path('', search_flights, name='search-flights'),
]