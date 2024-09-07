from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'skillType')
    list_filter = ('skillType',)
    search_fields = ('id', 'name', 'skillType')
    ordering = ('skillType', 'id',)