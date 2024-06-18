from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers


class User(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    timezone = models.CharField(max_length=128, default="Asia/Kathmandu")
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.username

    @staticmethod
    def validate_unique_email(value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
