from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

class PermissionTest(TestCase):
    def setUp(self):
        self.client = Client()
        # create groups
        Group.objects.get_or_create(name='viewer')
        Group.objects.get_or_create(name='manager')
        Group.objects.get_or_create(name='admin')

        # create users
        self.viewer = User.objects.create_user(username='v', password='v')
        self.manager = User.objects.create_user(username='m', password='m')
        self.admin = User.objects.create_user(username='a', password='a')

        # assign groups
        Group.objects.get(name='viewer').user_set.add(self.viewer)
        Group.objects.get(name='manager').user_set.add(self.manager)
        Group.objects.get(name='admin').user_set.add(self.admin)

    def test_viewer_cannot_create_asset(self):
        self.client.login(username='v', password='v')
        resp = self.client.get(reverse('asset_create'))
        # viewer should be redirected away (dashboard)
        self.assertEqual(resp.status_code, 302)

    def test_manager_can_create_asset(self):
        self.client.login(username='m', password='m')
        resp = self.client.get(reverse('asset_create'))
        self.assertEqual(resp.status_code, 200)

    def test_admin_can_delete_asset(self):
        # create a sample asset
        from .models import Asset
        asset = Asset.objects.create(name='X', value=1.0)
        self.client.login(username='a', password='a')
        resp = self.client.get(reverse('asset_delete', args=[asset.pk]))
        self.assertEqual(resp.status_code, 200)
