from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from topics.models import Topic, Category
from topics.serializers import TopicSerializer, CategorySerializer
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
import pytz


class TopicModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com", password="testpassword"
        )
        self.category = Category.objects.create(
            name="Test Category", user=self.user, active=True
        )
        self.topic = Topic.objects.create(
            user=self.user,
            title="Test Title",
            description="Test Description",
            category=self.category,
        )

    def test_topic_model(self):
        self.assertEqual(self.topic.user, self.user)
        self.assertEqual(self.topic.title, "Test Title")
        self.assertEqual(self.topic.description, "Test Description")
        self.assertEqual(self.topic.category, self.category)
        self.assertTrue(isinstance(self.topic.created_at, datetime.datetime))
        self.assertTrue(isinstance(self.topic.updated_at, datetime.datetime))


class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@test.com", password="testpassword"
        )

        self.category = Category.objects.create(
            name="Test Category", user=self.user, active=True
        )

    def test_category_model(self):
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.user, self.user)
