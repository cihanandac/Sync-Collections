from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("syncadlib", views.syncadlib, name='sync_adlib'),
    path("syncStartPlone", views.syncStartPlone, name='sync_start_plone'),
    path("syncStartAdlib", views.syncStartAdlib, name='sync_start_api'),
    path("stopsync", views.stopsync, name='stop_sync'),
    path("delete_plone_dates", views.delete_plone_dates, name='delete_plone_dates'),
    path('sync_status', views.sync_status, name='sync_status'),
    path("manualsync/", views.manualsync, name='manualsync'),
    path('not_synced/', views.not_synced_objects, name='not_synced'),
    path('check_status/<str:ccObjectID>/', views.check_status, name='check_status'),
    path('all/', views.index, name='all_objects'),
    path('show_museum_object_logs/<int:object_id>/',
         views.show_museum_object_logs, name='show_museum_object_logs'),
]
