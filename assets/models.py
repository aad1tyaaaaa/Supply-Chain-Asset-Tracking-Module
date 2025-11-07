from django.db import models
from django.utils import timezone


class Asset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class AssetLocation(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='locations')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='assets')
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=['asset', 'timestamp']),
            models.Index(fields=['location', 'timestamp']),
        ]
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.asset.name} at {self.location.name} on {self.timestamp}"
