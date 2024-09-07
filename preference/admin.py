from django.contrib import admin
from .models import *

@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'mediaType', 'contentType', 'learningType', 'timePerWeek', 'timePerSession']
    list_filter = ['id', 'mediaType', 'contentType', 'learningType', 'timePerWeek', 'timePerSession']
    search_fields = ['id', 'mediaType', 'contentType', 'learningType']