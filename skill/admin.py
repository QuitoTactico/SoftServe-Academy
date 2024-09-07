from django.contrib import admin
from .models import Skill, SkillLevel

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'skillType')
    list_filter = ('skillType',)
    search_fields = ('id', 'name', 'skillType')
    ordering = ('skillType', 'id',)

@admin.register(SkillLevel)
class SkillLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill', 'level')
    list_filter = ('skill', 'level')
    search_fields = ('id', 'skill', 'level')
    ordering = ('skill', 'level', 'id',)