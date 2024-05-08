from django.apps import AppConfig
from django.db.utils import OperationalError


class CollectionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "collection"

    def ready(self):
        # Import the SyncLock model within the ready method
        from .models import SyncLock
        try:
            # Retrieve the singleton lock and set `is_locked` to False
            lock, _ = SyncLock.objects.get_or_create(id=1)
            lock.is_locked = False
            lock.save()
        except OperationalError:
            # Catch exceptions if the database is not set up yet
            print("SyncLock table does not exist yet or is not yet migrated.")
