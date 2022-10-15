from django.contrib import admin
from .models import Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_cost', 'album_cost', 'approved']
    readonly_fields = ['creation_date']
 