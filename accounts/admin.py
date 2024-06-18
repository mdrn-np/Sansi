from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["username", "email", "name", "is_staff"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name", "timezone")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("name", "timezone")}),
    )


admin.site.register(User, CustomUserAdmin)
