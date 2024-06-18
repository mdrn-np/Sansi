from django.db import models
from django.utils import timezone
from main.settings import AUTH_USER_MODEL
import pytz


class Todo(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    discription = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    important = models.BooleanField(default=False)
    repetaion = models.CharField(max_length=200, blank=True, null=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        user_timezone = self.user.timezone
        now = timezone.now().astimezone(pytz.timezone(user_timezone))
        if not self.id:
            self.created_at = now
        self.updated_at = now
        if self.due_date:
            self.due_date = self.due_date.astimezone(pytz.timezone(user_timezone))
        super().save(*args, **kwargs)

    @property
    def past_due(self):
        return self.due_date and self.due_date < timezone.now()

    def __str__(self):
        return self.title
