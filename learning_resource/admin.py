from django.contrib import admin
from .models import LearningResource

# id: int
# name: string
# mediaType: enum
# contentType: enum
# link: string
# details: string
# duration: int
# language: enum
# originalPlatform: string
# originalAuthor: string
# contentManager: ContentManager
# generalLevel: int
# learningSkills: resourceLearningSkill[]
# requiredSkills: resourceRequiredSkill[] 
# reviews: Review[]

@admin.register(LearningResource)
class LearningResourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mediaType', 'contentType', 'link', 'details', 'duration', 'language', 'originalPlatform', 'originalAuthor', 'generalLevel']
    search_fields = ['id', 'name', 'mediaType', 'contentType', 'link', 'details', 'duration', 'language', 'originalPlatform', 'originalAuthor', 'generalLevel']
    list_filter = ['id', 'name', 'mediaType', 'contentType', 'link', 'details', 'duration', 'language', 'originalPlatform', 'originalAuthor', 'generalLevel']