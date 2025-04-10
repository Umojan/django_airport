from rest_framework import serializers
from .models import StoryBanner, InfoSection, InfoBanner

class StoryBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryBanner
        fields = ['id', 'name', 'image', 'is_active']

class InfoBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoBanner
        fields = ['id', 'title', 'description', 'content', 'image', 'is_active']


class InfoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoSection
        fields = ['id', 'title_ru', 'title_en', 'content_ru', 'content_en', 'image']
