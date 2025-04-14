from django.db import models

class Service(models.Model):
    SERVICE_TYPES = [
        ('jewelry', 'Ювелирка'),
        ('dutyfree', 'Duty-free'),
        ('souvenirs', 'Сувениры'),
        ('simcard', 'SIM-card'),
    ]

    # Основное название и переводы
    name_ru = models.CharField("Название (русский)", max_length=100)
    name_en = models.CharField("Название (английский)", max_length=100, blank=True)
    name_ky = models.CharField("Название (кыргызский)", max_length=100, blank=True)

    service_type = models.CharField(max_length=10, choices=SERVICE_TYPES)

    # Описание и переводы
    description_ru = models.TextField("Описание (русский)", blank=True)
    description_en = models.TextField("Описание (английский)", blank=True)
    description_ky = models.TextField("Описание (кыргызский)", blank=True)

    location = models.CharField(max_length=100)
    open_time = models.TimeField()
    close_time = models.TimeField()

    image = models.ImageField(upload_to='service_images/', blank=True, null=True)

    def __str__(self):
        # Выбираем название в зависимости от текущего языка
        from django.utils import translation
        current_language = translation.get_language()
        if current_language == 'en' and self.name_en:
            return f"{self.name_en} ({self.get_service_type_display()})"
        elif current_language == 'ky' and self.name_ky:
            return f"{self.name_ky} ({self.get_service_type_display()})"
        else:
            return f"{self.name_ru} ({self.get_service_type_display()})"