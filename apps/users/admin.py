from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.users.models import User

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)