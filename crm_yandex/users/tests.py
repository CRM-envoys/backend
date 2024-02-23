from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    """Тесты для модели CustomUser."""

    def test_create_user(self):
        """Тест создания обычного пользователя."""
        User = get_user_model()
        user = User.objects.create_user(
            username="Иван", email="ivan@i.com", password="testpass123"
        )
        self.assertEqual(user.username, "Иван")
        self.assertEqual(user.email, "ivan@i.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Тест создания суперпользователя."""
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superuser", email="superuser@i.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superuser")
        self.assertEqual(admin_user.email, "superuser@i.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
