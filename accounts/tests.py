from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="will", email="will@test.com", password="testpass123", name="Will"
        )
        self.assertEqual(user.username, "will")
        self.assertEqual(user.email, "will@test.com")
        self.assertTrue(user.is_active)
        self.assertEqual(user.name, "Will")
