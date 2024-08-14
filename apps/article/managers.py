from django.db.models import Manager
from django.utils import timezone

from apps.article.choices import Status


class PublishManager(Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(status=Status.PUBLISHED)
        return queryset


class AdvertiseManager(Manager):
    def active(self):
        """Return all active advertisements that are not expired."""
        return self.filter(is_active=True, expire__gte=timezone.now())

    def expired(self):
        """Return all advertisements that are expired."""
        return self.filter(expire__lt=timezone.now())

