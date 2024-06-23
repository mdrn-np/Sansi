from rest_framework import serializers
from topics.models import Topic, Category
from django.utils import timezone
import datetime
import pytz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    show = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = (
            "id",
            "user",
            "title",
            "description",
            "category",
            "created_at",
            "updated_at",
            "show",
        )

    def get_show(self, obj):
        user_tz = obj.user.tz
        tz = pytz.timezone(user_tz)
        now = timezone.now().astimezone(tz)
        creation_date = obj.created._astimezone(tz)
        delta = (now - creation_date).days
        return delta in {0, 1, 6, 29}
