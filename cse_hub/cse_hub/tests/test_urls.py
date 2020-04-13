from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from django.urls import reverse

class TestUrls(SimpleTestCase):

	def setUp(self):
		self.client = Client()

	def test_home_url_response_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage/homepage.html')

	def test_admin_url_response_status_code(self):
		response = self.client.get('/admin/')
		# such url mapping exists
		self.assertEqual(response.status_code, 302)
		# if user is not logged in, one should be redirected
		self.assertRedirects(response, '/admin/login/?next=/admin/')
		
	def test_editor_url_status_code(self):
		response = self.client.get('/editor/')
		self.assertTrue(response.status_code, 200)

	def test_editor_template(self):
		response = self.client.get('/editor/')
		self.assertTemplateUsed(response, 'homepage/editor.html')

	def test_editor_name(self):
		name = reverse('code-editor')
		path = '/editor/'
		self.assertEqual(path, name)

	def test_profile_redirect(self):
		response = self.client.get('/profile/someuser/')
		self.assertRedirects(response, '/login/?next=/profile/someuser/')
		# check if status code is for redirect
		self.assertEqual(response.status_code, 302)

	def test_logout_status_code(self):
		response = self.client.get('/logout/')
		self.assertEqual(response.status_code, 200)

	def test_logout_template(self):
		response = self.client.get('/logout/')
		self.assertTemplateUsed(response, 'users/logout.html')


class TestDatabaseQueryingUrls(TestCase):

	def setUp(self):
		self.client = Client()

	def test_problem_url_status_code(self):
		response = self.client.get('/problems/')
		self.assertEqual(response.status_code, 200)

	def test_problem_template(self):
		response = self.client.get('/problems/')
		self.assertTemplateUsed(response, 'problems/display_problems.html')

	def test_forum_url_status_code(self):
		response = self.client.get('/forum/')
		self.assertEqual(response.status_code, 200)

	def test_forum_template(self):
		response = self.client.get('/forum/')
		self.assertTemplateUsed(response, 'forum/home.html')
