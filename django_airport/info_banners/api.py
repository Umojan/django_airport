from rest_framework.routers import DefaultRouter
from .views import StoryBannerViewSet, InfoBannerViewSet

router = DefaultRouter()
router.register(r'story-banners', StoryBannerViewSet, basename='story-banner')
router.register(r'info-banners', InfoBannerViewSet, basename='info-banner')