from django.contrib import admin
from .models import Album, Genre, Track


class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'artist',
        'genre',
        'release_year',
        'price',
        'special_edition',
    )

    ordering = ('title',)


class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'album',
        'title',
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Track, TrackAdmin)
