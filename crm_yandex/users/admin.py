from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Админ зона для модели User."""

    model = CustomUser

    readonly_fields = (
        "last_login",
        "date_joined",
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    list_filter = (
        "email",
        "first_name",
        "last_name",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    empty_value_display = "-пусто-"
    ordering = ("-id",)
