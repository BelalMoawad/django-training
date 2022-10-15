from django.db import models
from datetime import date
from artists.models import Artist

class Album(models.Model) :
    album_name = models.CharField(max_length = 30, default="New Album")
    creation_date = models.DateField(auto_now_add=True)
    releasing_date = models.DateField()
    album_cost = models.FloatField(blank = True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    approved = models.BooleanField(default=False, help_text = "Approve the album if its name is not explicit")

    def __str__(self) :
        return self.album_name