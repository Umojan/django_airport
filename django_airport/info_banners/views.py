from rest_framework import viewsets
from .models import StoryBanner, InfoBanner, InfoSection
from .serializers import StoryBannerSerializer, InfoBannerSerializer, InfoSectionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class StoryBannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StoryBanner.objects.filter(is_active=True)
    serializer_class = StoryBannerSerializer

class InfoBannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InfoBanner.objects.filter(is_active=True)
    serializer_class = InfoBannerSerializer

    @action(detail=True, methods=['get'])
    def content(self, request, pk=None):
        info_banner = self.get_object()
        return Response({'content': info_banner.content})

class InfoSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InfoSection.objects.filter(is_active=True)
    serializer_class = InfoSectionSerializer