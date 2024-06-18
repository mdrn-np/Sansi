from rest_framework import serializers
from django.utils import timezone
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    is_due = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = [
            "id",
            "user",
            "title",
            "discription",
            "category",
            "important",
            "repetaion",
            "due_date",
            "completed",
            "is_due",
        ]

    def get_is_due(self, obj):
        return timezone.now() > obj.due_date if obj.due_date else False
