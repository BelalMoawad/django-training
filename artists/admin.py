from django.contrib import admin
from albums.models import Album
from .models import Artist
from django.utils.html import format_html

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 0

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display= ['stageName','socialLink','approvedAlbums']
    list_per_page = 8
    inlines = [AlbumInline, ]

    def socialLink(self, artist):
        return format_html('<a href={}>{}</a>', artist.social_link, artist.social_link)
    
    def approvedAlbums(self, artist):
        cnt = 0
        for album in artist.albums.all():
            if album.approved == 1:
                cnt += 1

        return cnt