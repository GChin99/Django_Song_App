from django.db import models

# Create your models here.

class Album(models.Model):
    album_name = models.CharField()
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)