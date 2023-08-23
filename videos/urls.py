# videos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.video_search, name='video_search'),
    path('saved-videos/', views.saved_videos, name='saved_videos'),
    path('save/<int:video_id>/', views.save_video, name='save_video'),
    path('unsaved/<int:video_id>/', views.mark_as_unsaved, name='mark_as_unsaved'),
    path('watched/', views.watched_videos, name='watched_videos'),
    path('mark_as_watched/<int:video_id>/', views.mark_as_watched, name='mark_as_watched'),
    path('mark_as_unwatched/<int:video_id>/', views.mark_as_unwatched, name='mark_as_unwatched'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),  # Add this line
]
