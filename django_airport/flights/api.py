from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, search_flights
from django.urls import path

router = DefaultRouter()
router.register(r'', FlightViewSet, basename='flight')
router.register(r'flights', FlightViewSet, basename='flight')

urlpatterns = router.urls + [
    path('search/', search_flights, name='search-flights'),
]