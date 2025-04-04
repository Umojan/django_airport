from django.db import models

class Service(models.Model):
    SERVICE_TYPES = [
        ('jewelry', 'Ювелирка'),
        ('dutyfree', 'Duty-free'),
        ('souvenirs', 'Сувениры'),
        ('simcard', 'SIM-card'),
    ]

    name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPES)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=100)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.get_service_type_display()})"