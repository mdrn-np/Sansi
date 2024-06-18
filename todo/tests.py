from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Todo
from datetime import datetime
import pytz


class TodoModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="testuser", password="12345", timezone="UTC"
        )
        self.todo = Todo.objects.create(
            user=user,
            title="Test todo",
            discription="Test todo Description",
            category="Test todo Category",
            important=True,
            repetaion="Test todo Repetaion",
            due_date=datetime.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"),
        )

    def test_todo_model(self):
        self.assertEqual(self.todo.title, "Test todo")
        self.assertEqual(self.todo.discription, "Test todo Description")
        self.assertEqual(self.todo.category, "Test todo Category")
        self.assertEqual(self.todo.important, True)
        self.assertEqual(self.todo.repetaion, "Test todo Repetaion")
        self.assertEqual(str(self.todo), "Test todo")
        self.assertEqual(self.todo.past_due, True)

    def test_todo_save(self):
        self.todo.title = "New Test todo"
        self.todo.save()
        self.assertEqual(self.todo.title, "New Test todo")
        self.assertEqual(self.todo.past_due, True)
        self.todo.due_date = datetime.strptime(
            "2025-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"
        )
        self.todo.save()
        self.assertEqual(self.todo.past_due, False)
