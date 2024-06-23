from django.contrib import admin
from .models import Category, Topic


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "category",
        "created_at",
        "updated_at",
        "user.tz",
    )
    search_fields = ("title", "category")
    ordering = ("title",)


admin.site.register(Category, CategoryAdmin)
