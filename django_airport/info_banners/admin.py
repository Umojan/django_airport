from django.contrib import admin
from .models import StoryBanner, InfoBanner, InfoSection

@admin.register(StoryBanner)
class StoryBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(InfoBanner)
class InfoBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)

@admin.register(InfoSection)
class InfoSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ru', 'title_en', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title_ru', 'title_en')

