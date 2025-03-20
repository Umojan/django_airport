from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'location', 'open_time', 'close_time')
    list_filter = ('service_type', 'location')
    search_fields = ('name', 'description', 'location')