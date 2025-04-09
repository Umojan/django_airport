from django.db import models
from ckeditor.fields import RichTextField

class StoryBanner(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='story_banners/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class InfoBanner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='info_banners/', null=True, blank=True)
    content = RichTextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class InfoSection(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    image = models.ImageField(upload_to="info_sections/")
    content_ru = RichTextField()
    content_en = RichTextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_ru
