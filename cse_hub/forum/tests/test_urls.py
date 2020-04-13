from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from django.urls import reverse, resolve
from forum.views import home

class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_name_for_forum_home(self):
        name = reverse('forum-home')
        path = '/forum/'
        self.assertEqual(path, name)

    def test_forum_home_resolves_to_home_view(self):
        response = resolve('/forum/')
        self.assertEqual(response.func, home)

    