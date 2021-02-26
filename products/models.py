from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Format(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Album(models.Model):
    genre = models.ForeignKey('Genre', null=True, blank=True,
                              on_delete=models.SET_NULL)
    avg_rating = models.FloatField(default=0)
    title = models.CharField(max_length=254)
    sku = models.CharField(max_length=254, null=True, blank=True)
    artist = models.CharField(max_length=254)
    release_year = models.IntegerField()
    EIGHTIES = 1980
    NINETIES = 1990
    ZEROS = 2000
    TENS = 2010
    TWENTIES = 2020
    ERA_CHOICES = [
        (EIGHTIES, '1980'),
        (NINETIES, '1990'),
        (ZEROS, '2000'),
        (TENS, '2010'),
        (TWENTIES, '2020'),
    ]
    era = models.IntegerField(choices=ERA_CHOICES, default=1990)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    special_edition = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    album_format = models.ForeignKey('Format', null=True, blank=True,
                                     on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey('Album', null=True, blank=True,
                              on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)

    def __str__(self):
        return self.title


class Review(models.Model):
    album = models.ForeignKey('Album', null=True, blank=True,
                              on_delete=models.SET_NULL)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    album = models.ForeignKey('Album', null=True, blank=True,
                              on_delete=models.SET_NULL)
    rating = models.PositiveSmallIntegerField()
    review = models.OneToOneField('Review', null=True, blank=True,
                                  on_delete=models.CASCADE)
