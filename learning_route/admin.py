from django.contrib import admin
from .models import LearningRoute, LearningRouteResource

admin.site.register(LearningRoute)
admin.site.register(LearningRouteResource)

'''
@admin.register(LearningRoute)
class LearningRouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_level', 'duration', 'completed', 'time_spent')
    list_filter = ('skill_level__skill__name', 'completed')
    search_fields = ('id', 'skill_level', 'duration', 'completed')

@admin.register(LearningRouteResource)
class LearningRouteResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'completed', 'time_spent')
    list_filter = ('completed',)
    search_fields = ('id', 'completed')
    ordering = ('completed', 'time_spent')
'''