from email.policy import default
from unicodedata import name
from django import forms

from albums.models import Album


class AlbumForm(forms.Form):
    album_name = forms.CharField(min_length = 8, max_length = 30)
    abum_date = forms.DateField()
    album_cost = forms.FloatField()
    