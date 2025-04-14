from django.db import models

class Flight(models.Model):
    is_arrival = models.BooleanField()  # True: прибытие, False: вылет
    airline = models.CharField(max_length=100)
    flight_code = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=100)
    arrival_city_en = models.CharField(max_length=100, blank=True)
    arrival_city_kg = models.CharField(max_length=100, blank=True)
    time = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.airline} {self.flight_code} ({self.arrival_city})"

    class Meta:
        db_table = 'flights_schedule'
