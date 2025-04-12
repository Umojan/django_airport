from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from flights.views import FlightViewSet
from services.views import ServiceViewSet

from info_banners.api import router as info_banners_router

router = DefaultRouter()
router.register(r'flights', FlightViewSet, basename='flight')
router.register(r'services', ServiceViewSet, basename='service')

# объединяем роутеры
router.registry.extend(info_banners_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/flights/search/', include('flights.search_urls')),  # отдельный модуль для поиска
    path('api/', include(router.urls)),  # основной роутер
    path('api/flights/', include('flights.urls')),  # если там уже есть другие маршруты
    path('api/chat/', include('chat.urls')),
    path('api/auth/', include('users.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
