from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "is_superuser"]
    list_filter = [
        "id",
        "name",
        "learning_routes__skill_level__skill__name",
        "is_superuser",
    ]
    search_fields = ["id", "name", "email"]
    list_display_links = ["id", "name"]
