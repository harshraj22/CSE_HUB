# https://stackoverflow.com/a/11887308/10127204
from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from django.urls import reverse, resolve

class TestViews(TestCase):
    def setUp(self):
        pass

    # def 