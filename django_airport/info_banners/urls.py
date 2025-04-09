from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoryBannerViewSet, InfoBannerViewSet, InfoSectionViewSet

router = DefaultRouter()
router.register(r'story-banners', StoryBannerViewSet, basename='story-banner')
router.register(r'info-banners', InfoBannerViewSet, basename='info-banner')
router.register(r'info-sections', InfoSectionViewSet, basename='info-sections')

urlpatterns = [
    path('', include(router.urls)),
]