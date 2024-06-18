from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    timezone = models.CharField(max_length=128, default="Asia/Kathmandu")

    def __str__(self):
        return self.username
