from django.contrib import admin
from .models import Skill, SkillLevel


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "skill_type"]
    list_filter = ["skill_type"]
    search_fields = ["id", "name", "skill_type"]
    list_display_links = ["id", "name"]


@admin.register(SkillLevel)
class SkillLevelAdmin(admin.ModelAdmin):
    list_display = ["id", "skill", "level"]
    list_filter = ["skill", "level"]
    search_fields = ["id", "skill", "level"]
    list_display_links = ["id", "skill"]
