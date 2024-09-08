from django.contrib import admin
from .models import LearningRoute, LearningRouteResource

@admin.register(LearningRoute)
class LearningRouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_level', 'duration', 'completed', 'time_spent')
    list_filter = ('skill_level', 'completed')
    search_fields = ('id', 'skill_level', 'duration', 'completed')

@admin.register(LearningRouteResource)
class LearningRouteResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'learning_route', 'learning_resource', 'completed', 'time_spent')
    list_filter = ('learning_route', 'completed')
    search_fields = ('id', 'learning_route', 'learning_resource', 'completed')
    ordering = ('learning_route', 'completed', 'time_spent')