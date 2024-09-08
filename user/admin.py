from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_filter = ['id', 'name', 'learning_routes__skill_level__skill__name']
    search_fields = ['id', 'name', 'email']
    list_display_links = ['id', 'name']
