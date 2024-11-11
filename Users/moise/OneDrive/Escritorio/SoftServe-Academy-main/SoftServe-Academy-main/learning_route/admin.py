from django.contrib import admin
from .models import LearningRoute, LearningRouteResource


@admin.register(LearningRoute)
class LearningRouteAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "skill_level",
        "duration",
        "actual_resource_index",
        "completed",
        "time_spent",
    ]
    list_filter = ["skill_level__skill__name", "users_route", "completed"]
    search_fields = ["id", "skill_level", "duration", "completed"]
    list_display_links = ["id", "skill_level"]


@admin.register(LearningRouteResource)
class LearningRouteResourceAdmin(admin.ModelAdmin):
    list_display = ["id", "learning_resource", "completed", "time_spent"]
    list_filter = ["completed", "learning_resource__required_skills__skill__name"]
    search_fields = ["id", "completed"]
