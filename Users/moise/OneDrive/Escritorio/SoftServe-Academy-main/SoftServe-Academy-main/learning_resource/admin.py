from django.contrib import admin
from .models import LearningResource, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "rate", "created_at", "comment"]
    search_fields = [
        "id",
        "user",
        "rate",
        "created_at",
        "comment",
        "learning_resource_review",
    ]
    list_filter = ["rate", "created_at", "comment", "user"]
    list_display_links = ["id", "user", "rate"]


@admin.register(LearningResource)
class LearningResourceAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "media_type",
        "content_type",
        "link",
        "duration",
        "language",
        "original_platform",
        "original_author",
        "general_level",
    ]
    search_fields = [
        "id",
        "name",
        "media_type",
        "content_type",
        "link",
        "details",
        "duration",
        "language",
        "original_platform",
        "original_author",
        "general_level",
    ]
    list_filter = [
        "id",
        "name",
        "media_type",
        "content_type",
        "link",
        "details",
        "duration",
        "language",
        "original_platform",
        "original_author",
        "general_level",
    ]
    list_display_links = ["id", "name"]
