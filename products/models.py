from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_fiendly_name(self):
        return self.friendly_name


class Album(models.Model):
    genre = models.ForeignKey('Genre', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    artist = models.CharField(max_length=254)
    release_year = models.IntegerField()
    era = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    special_edition = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey('Album', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)

    def __str__(self):
        return self.title
