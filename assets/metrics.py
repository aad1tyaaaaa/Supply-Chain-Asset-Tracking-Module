from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from django.http import JsonResponse
from django.views.decorators.cache import never_cache
from django.urls import reverse
import time
from collections import deque
from statistics import mean, median
import psutil
import os

# Simple metrics store (reset on server restart, which is fine for demo)
METRICS = {
    'cache_hits': 0,
    'cache_misses': 0,
    'cache_hit_ratio': 0.0,
    'cache_keys': 0,
    'response_times': deque(maxlen=100),  # Keep last 100 response times
    'requests_per_minute': 0,
    'last_minute_requests': deque(maxlen=60),  # Track requests in last minute
    'process_memory': 0,
}

class MetricsMiddleware:
    """Track cache hits/misses and other metrics."""
    def __init__(self, get_response):
        self.get_response = get_response
        # Initialize metrics (handle test resets)
        METRICS['cache_hits'] = 0
        METRICS['cache_misses'] = 0
        METRICS['cache_hit_ratio'] = 0.0
        METRICS['cache_keys'] = 0
        METRICS['response_times'].clear()
        METRICS['last_minute_requests'].clear()
        METRICS['requests_per_minute'] = 0
        METRICS['process_memory'] = 0

    def __call__(self, request):
        # Record request start time
        start_time = time.time()
        
        # Process request (before view)
        keys_before = 0
        if hasattr(cache, '_cache'):
            try:
                keys_before = len(cache._cache)
            except (TypeError, AttributeError):
                pass

        response = self.get_response(request)

        # Calculate response time
        response_time = time.time() - start_time
        METRICS['response_times'].append(response_time)
        
        # Update request rate
        current_time = int(time.time())
        METRICS['last_minute_requests'].append(current_time)
        # Remove requests older than 60 seconds
        while METRICS['last_minute_requests'] and METRICS['last_minute_requests'][0] < current_time - 60:
            METRICS['last_minute_requests'].popleft()
        METRICS['requests_per_minute'] = len(METRICS['last_minute_requests'])

        # Update memory usage
        process = psutil.Process(os.getpid())
        METRICS['process_memory'] = process.memory_info().rss

        # Update metrics after view
        keys_after = 0
        if hasattr(cache, '_cache'):
            try:
                keys_after = len(cache._cache)
            except (TypeError, AttributeError):
                pass

        # Track cache activity on cacheable views
        if request.path == reverse('dashboard'):
            if keys_after > keys_before:
                METRICS['cache_misses'] += 1
            elif keys_after == keys_before and keys_after > 0:
                METRICS['cache_hits'] += 1

        METRICS['cache_keys'] = keys_after
        total = METRICS['cache_hits'] + METRICS['cache_misses']
        if total > 0:
            METRICS['cache_hit_ratio'] = METRICS['cache_hits'] / total

        return response

@never_cache
def metrics_view(request):
    """
    Enhanced Prometheus-style metrics endpoint.
    
    Provides detailed metrics about:
    - Cache performance (hits, misses, ratio)
    - Response times (avg, median, p95)
    - Request rates
    - Memory usage
    """
    response_times = list(METRICS['response_times'])
    response_time_stats = {
        'avg': mean(response_times) if response_times else 0,
        'median': median(response_times) if response_times else 0,
        'p95': sorted(response_times)[int(len(response_times) * 0.95)] if len(response_times) >= 20 else 0
    }

    return JsonResponse({
        # Cache metrics
        'cache_hits': METRICS['cache_hits'],
        'cache_misses': METRICS['cache_misses'],
        'cache_hit_ratio': METRICS['cache_hit_ratio'],
        'cache_keys': METRICS['cache_keys'],
        
        # Performance metrics
        'response_time_avg': response_time_stats['avg'],
        'response_time_median': response_time_stats['median'],
        'response_time_p95': response_time_stats['p95'],
        'requests_per_minute': METRICS['requests_per_minute'],
        
        # Resource usage
        'process_memory_bytes': METRICS['process_memory'],
        'process_memory_mb': METRICS['process_memory'] / (1024 * 1024),
        
        # Cache memory from Redis (if available)
        'cache_memory_used': cache.info().get('used_memory', 0) if hasattr(cache, 'info') else 0,
    })