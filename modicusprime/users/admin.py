from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()


class CustomUserAdmin(auth_admin.UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "last_login",
    )
    search_fields = ("username", "email")

    readonly_fields = [
        "last_login",
    ]


admin.site.register(User, CustomUserAdmin)
