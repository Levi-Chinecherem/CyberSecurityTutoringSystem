
# videos/models.py

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100)
    video_url = models.URLField()
    thumbnail = models.URLField(max_length=500) 
    watched = models.BooleanField(default=False)  # Field to mark if the video is watched
    saved = models.BooleanField(default=False)    # Field to mark if the video is saved

    def __str__(self):
        return self.title
