from django.db import models
from datetime import date
from artists.models import Artist

class Album(models.Model) :
    album_name = models.CharField(max_length = 30)
    abum_date = models.DateField()
    album_cost = models.FloatField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self) :
        return self.album_name