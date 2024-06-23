from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "tz")
    search_fields = ("email", "username")
    readonly_fields = ("date_joined", "last_login")
    ordering = ("email",)


admin.site.register(User, UserAdmin)
