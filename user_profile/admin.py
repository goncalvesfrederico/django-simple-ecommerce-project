from django.contrib import admin
from user_profile.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = "user", "cpf", "address", "number", "neighborhood", "city", "state"
    list_display_links = "user", "cpf",
    search_fields = "user",
    ordering = "-pk",