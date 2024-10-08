from django.contrib import admin
from .models import *


@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "media_type",
        "content_type",
        "learning_type",
        "time_per_week",
        "time_per_session",
    ]
    list_filter = [
        "media_type",
        "content_type",
        "learning_type",
        "time_per_week",
        "time_per_session",
    ]
    search_fields = ["id", "media_type", "content_type", "learning_type"]
    list_display_links = ["id", "media_type", "content_type", "learning_type"]
