from django.contrib import admin
from .models import LearningResource

@admin.register(LearningResource)
class LearningResourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'media_type', 'content_type', 'link', 'duration', 'language', 'original_platform', 'original_author', 'general_level']
    search_fields = ['id', 'name', 'media_type', 'content_type', 'link', 'details', 'duration', 'language', 'original_platform', 'original_author', 'general_level']
    list_filter = ['id', 'name', 'media_type', 'content_type', 'link', 'details', 'duration', 'language', 'original_platform', 'original_author', 'general_level']