from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #all_song from the song class will be added here

# One to many relationship
class Song(models.Model):
    song_name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name="all_songs", on_delete = models.CASCADE)  #this links the songs class to the album class 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)