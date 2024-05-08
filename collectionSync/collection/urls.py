from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("syncadlib", views.syncadlib, name='sync_adlib'),
    path("stopsync", views.stopsync, name='stop_sync'),
    path("delete_plone_dates", views.delete_plone_dates, name='delete_plone_dates'),
    path('sync_status', views.sync_status, name='sync_status'),
    path("manualsync/<str:ccObjectID>/<str:ccIndexName>", views.manualsync, name='manualsync'),
    path('not_synced/', views.not_synced_objects, name='not_synced'),
    path('check_status/<str:ccObjectID>/', views.check_status, name='check_status'),
    path('all/', views.all_objects, name='all_objects'),
]
