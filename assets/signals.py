from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Asset, AssetLocation

DASHBOARD_CACHE_KEY = '_dashboard_view'  # shared key used by cache_page on dashboard


def invalidate_dashboard():
    """Clear the dashboard cache so next request gets fresh data."""
    cache.delete(DASHBOARD_CACHE_KEY)


@receiver([post_save, post_delete], sender=Asset)
def handle_asset_change(sender, instance, **kwargs):
    """When assets are created/updated/deleted, invalidate the dashboard cache."""
    invalidate_dashboard()


@receiver([post_save, post_delete], sender=AssetLocation)
def handle_movement_change(sender, instance, **kwargs):
    """When movements are recorded/updated/deleted, invalidate the dashboard cache."""
    invalidate_dashboard()