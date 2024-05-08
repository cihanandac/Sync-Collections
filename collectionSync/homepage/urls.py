from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('logs', views.view_logs,
         name='view_sync_start_log'),
]
