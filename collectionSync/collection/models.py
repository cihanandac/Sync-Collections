from django.db import models


class MuseumObject(models.Model):
    title = models.CharField(default="", max_length=50, null=True, blank=True)
    ccObjectID = models.CharField(default="", db_index=True, max_length=50,)
    api_lastmodified = models.DateTimeField(null=True, blank=True,)
    plone_timestamp = models.DateTimeField(null=True, blank=True,)
    index_name = models.CharField(default="", max_length=50,)
    synced = models.BooleanField(null=True,)

    def save(self, *args, **kwargs):
        # Update `synced` based on the comparison of `api_lastmodified` and `plone_timestamp`
        if self.api_lastmodified == self.plone_timestamp:
            self.synced = True
        else:
            self.synced = False
        
        super(MuseumObject, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.title}"


class SyncLock(models.Model):
    sync_switch = models.CharField(default="sync_switch", max_length=50)
    is_locked = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    stop_requested = models.BooleanField(default=False)

    def __str__(self):
        return f"Lock status: {'Locked' if self.is_locked else 'Unlocked'}"


class ObjectLog(models.Model):
    museum_object = models.ForeignKey(
        MuseumObject, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    log_message = models.TextField()

    def __str__(self):
        return f"Log for {self.museum_object.ccObjectID} at {self.timestamp}"

    @staticmethod
    def cleanup_old_logs(museum_object, limit=10):
        logs = ObjectLog.objects.filter(
            museum_object=museum_object).order_by('-timestamp')
        if logs.count() > limit:
            for log in logs[limit:]:
                log.delete()
