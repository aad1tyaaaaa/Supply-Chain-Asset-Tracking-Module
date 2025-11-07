from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.cache import cache

User = get_user_model()

class AuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        cache.clear()
        # create a test user
        self.username = 'tester'
        self.password = 'password123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_dashboard_requires_login(self):
        # Unauthenticated should redirect to login
        resp = self.client.get(reverse('dashboard'))
        self.assertEqual(resp.status_code, 302)
        self.assertIn(reverse('login'), resp['Location'])

        # Login and access dashboard
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login)
        resp2 = self.client.get(reverse('dashboard'))
        self.assertEqual(resp2.status_code, 200)
        self.assertIn('Total assets', str(resp2.content))
