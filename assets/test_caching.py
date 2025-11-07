from django.test import TestCase, Client
from django.urls import reverse
from django.core.cache import cache
from .models import Asset
import time


class CachingTest(TestCase):
    def setUp(self):
        self.client = Client()
        cache.clear()  # ensure clean cache state
        # create and login a test user so protected views are accessible
        from django.contrib.auth import get_user_model
        User = get_user_model()
        self.user = User.objects.create_user(username='cacheuser', password='pass')
        self.client.login(username='cacheuser', password='pass')
    def test_dashboard_cache_invalidation(self):
        """Test that dashboard cache is invalidated when assets change."""
        cache.clear()  # ensure clean state

        # First request should be a cache miss
        resp1 = self.client.get(reverse('dashboard'))
        self.assertEqual(resp1.status_code, 200)
        self.assertIn('Total assets', str(resp1.content))
        self.assertIn('0', str(resp1.content))  # no assets yet

        # Create a new asset - should invalidate cache
        Asset.objects.create(name='New Asset', value=100.00)

        # Second request should show new asset (cache was invalidated)
        resp2 = self.client.get(reverse('dashboard'))
        self.assertEqual(resp2.status_code, 200)
        self.assertIn('Total assets', str(resp2.content))
        self.assertIn('1', str(resp2.content))  # one asset now

    def test_metrics_endpoint(self):
        """Test that metrics endpoint returns comprehensive stats."""
        cache.clear()  # ensure clean state

        # Make some cached and uncached requests with delays to test timing
        self.client.get(reverse('dashboard'))  # miss
        time.sleep(0.1)  # Ensure measurable response time
        self.client.get(reverse('dashboard'))  # hit
        self.client.get(reverse('asset_list'))  # uncached view

        resp = self.client.get(reverse('metrics'))
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        
        # Cache metrics
        self.assertIn('cache_hits', data)
        self.assertIn('cache_misses', data)
        self.assertGreaterEqual(data['cache_hits'] + data['cache_misses'], 1)
        
        # Performance metrics
        self.assertIn('response_time_avg', data)
        self.assertIn('response_time_median', data)
        self.assertIn('response_time_p95', data)
        self.assertIn('requests_per_minute', data)
        self.assertGreater(data['requests_per_minute'], 0)
        
        # Resource metrics
        self.assertIn('process_memory_bytes', data)
        self.assertIn('process_memory_mb', data)
        self.assertGreater(data['process_memory_bytes'], 0)
        self.assertGreater(data['process_memory_mb'], 0)