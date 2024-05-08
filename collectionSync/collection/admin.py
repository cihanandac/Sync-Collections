from django.contrib import admin
from .models import MuseumObject, SyncLock


class MuseumObjectAdmin(admin.ModelAdmin):
    list_filter = ("title", "ccObjectID", "index_name")
    list_display = ("title", "ccObjectID", "index_name", "synced")


class SyncLockAdmin(admin.ModelAdmin):
    list_display = ("sync_switch", "is_locked", "last_updated")
    readonly_fields = ("last_updated",)


# Register both models
admin.site.register(MuseumObject, MuseumObjectAdmin)
admin.site.register(SyncLock, SyncLockAdmin)
