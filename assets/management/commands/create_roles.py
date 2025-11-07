from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Create default user groups for the asset tracking app (admin, manager, viewer)'

    def handle(self, *args, **options):
        groups = ['admin', 'manager', 'viewer']
        for g in groups:
            group, created = Group.objects.get_or_create(name=g)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created group: {g}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Group already exists: {g}'))
        self.stdout.write(self.style.SUCCESS('Default groups ensured.'))
