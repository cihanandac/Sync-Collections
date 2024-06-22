from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from collection.models import SyncLock
from .utils import tail
import os


def index(request):
    sync_running = SyncLock.objects.get(id=1).is_locked
    return render(
        request,
        "homepage/index.html",
        {
            "sync_running": sync_running,
        },
    )


def view_logs(request):
    sync_running = SyncLock.objects.get(id=1).is_locked

    log_file_path = os.path.join(
        os.path.dirname(__file__), "..", "logs", "create_update_object.log"
    )
    log_lines = tail(log_file_path, 30)
    return render(
        request,
        "homepage/view_log.html",
        {"log_lines": log_lines, "sync_running": sync_running},
    )
