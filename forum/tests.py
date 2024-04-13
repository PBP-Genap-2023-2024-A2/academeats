from django.contrib.auth.models import User
from django.test import TestCase

from user_profile.models import Profile


class ForumTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='carlravel', email="carl@ui.ac.id", password="Farhan123456#")