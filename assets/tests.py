from django.test import TestCase
from django.urls import reverse
from .models import Asset, Location, AssetLocation
from django.utils import timezone


class AssetModelTest(TestCase):
	def test_str(self):
		a = Asset.objects.create(name='Drill', value=100.00)
		self.assertEqual(str(a), 'Drill')


class DashboardViewTest(TestCase):
	def setUp(self):
		self.loc = Location.objects.create(name='Warehouse', address='123 St')
		self.asset = Asset.objects.create(name='Truck', value=5000.00)
		AssetLocation.objects.create(asset=self.asset, location=self.loc, timestamp=timezone.now())
		# create and login a test user so protected views are accessible
		from django.contrib.auth import get_user_model
		User = get_user_model()
		self.user = User.objects.create_user(username='tester', password='password')
		self.client.login(username='tester', password='password')

	def test_dashboard_status(self):
		resp = self.client.get(reverse('dashboard'))
		self.assertEqual(resp.status_code, 200)
		self.assertContains(resp, 'Total assets')


class AssetFormAndPaginationTest(TestCase):
	def setUp(self):
		# create a location for asset movements
		self.loc = Location.objects.create(name='Depot', address='1 Road')
		# login user for protected views
		from django.contrib.auth import get_user_model
		User = get_user_model()
		self.user = User.objects.create_user(username='u1', password='pwd')
		self.client.login(username='u1', password='pwd')

	def test_create_asset_via_form(self):
		url = reverse('asset_create')
		data = {'name': 'Compressor', 'description': 'Air compressor', 'value': '250.00'}
		resp = self.client.post(url, data, follow=True)
		self.assertEqual(resp.status_code, 200)
		self.assertTrue(Asset.objects.filter(name='Compressor').exists())

	def test_asset_list_pagination(self):
		# create 25 assets to ensure pagination (paginate_by=10)
		for i in range(25):
			Asset.objects.create(name=f'Asset {i}', value=10.0 + i)

		url = reverse('asset_list')
		resp = self.client.get(url + '?page=1')
		self.assertEqual(resp.status_code, 200)
		# page 1 shows newest items (view orders by -created_at) and should contain 10 items
		# check that the newest and the 10th newest appear
		self.assertContains(resp, 'Asset 24')
		self.assertContains(resp, 'Asset 15')

