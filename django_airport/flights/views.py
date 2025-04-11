from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Flight
from .serializers import FlightSerializer
from .filters import FlightFilter
import requests
import os
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = FlightFilter  # Use the custom FlightFilter
    ordering_fields = ['time']  # Enables ordering by time



load_dotenv()

API_KEY = os.getenv("TRAVELPAYOUTS_API_KEY")
API_URL = "https://api.travelpayouts.com/v2/prices/latest"

@api_view(['GET'])
def search_flights(request):
    origin = request.GET.get('origin', 'FRU')  # Бишкек
    destination = request.GET.get('destination', 'LED')  # пример: Санкт-Петербург
    currency = request.GET.get('currency', 'usd')

    params = {
        "origin": origin,
        "destination": destination,
        "currency": currency,
        "limit": 10,
        "page": 1
    }

    headers = {
        "X-Access-Token": API_KEY,
    }

    try:
        response = requests.get(API_URL, params=params, headers=headers)
        data = response.json()
        return Response(data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)