from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "completed"]
    list_editable = ["completed"]

    class Meta:
        model = Todo


admin.site.register(Todo, TodoAdmin)
