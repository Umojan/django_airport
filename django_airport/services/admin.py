from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name_ru', 'name_en', 'name_ky', 'service_type', 'location', 'open_time', 'close_time'
    )
    list_filter = ('service_type',)
    search_fields = ('name_ru', 'name_en', 'name_ky', 'description_ru', 'description_en', 'description_ky')