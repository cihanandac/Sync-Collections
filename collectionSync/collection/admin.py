from django.contrib import admin
from .models import MuseumObject, SyncLock, ObjectLog


class MuseumObjectAdmin(admin.ModelAdmin):
    list_filter = ("title", "ccObjectID", "index_name")
    list_display = ("title", "ccObjectID", "index_name", "synced")


class SyncLockAdmin(admin.ModelAdmin):
    list_display = ("sync_switch", "is_locked", "last_updated")
    readonly_fields = ("last_updated",)


class ObjectLogAdmin(admin.ModelAdmin):
    list_display = ("museum_object", "timestamp", "log_message")
    list_filter = ("museum_object", "timestamp")
    search_fields = ("museum_object__ccObjectID", "log_message")

# Register both models
admin.site.register(MuseumObject, MuseumObjectAdmin)
admin.site.register(SyncLock, SyncLockAdmin)
admin.site.register(ObjectLog, ObjectLogAdmin)