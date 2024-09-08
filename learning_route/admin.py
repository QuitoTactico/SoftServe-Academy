from django.contrib import admin
from .models import LearningRoute, LearningRouteResource

@admin.register(LearningRoute)
class LearningRouteAdmin(admin.ModelAdmin):
    list_display = ('skillLevel', 'duration', 'completed', 'time_spent')
    list_filter = ('skillLevel', 'completed')
    search_fields = ('skillLevel', 'duration', 'completed')

@admin.register(LearningRouteResource)
class LearningRouteResourceAdmin(admin.ModelAdmin):
    list_display = ('LearningRoute', 'learning_resource', 'completed', 'time_spent')
    list_filter = ('LearningRoute', 'completed')
    search_fields = ('LearningRoute', 'learning_resource', 'completed')
    ordering = ('LearningRoute', 'completed', 'time_spent')