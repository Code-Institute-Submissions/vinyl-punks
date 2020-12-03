from django.shortcuts import render
from .models import Album, Track


def all_products(request):
    """ A view to display all albums """

    albums = Album.objects.all()
    print(albums)
    tracks = Track.objects.all()

    context = {
        'albums': albums,
        'tracks': tracks,
    }

    return render(request, 'products/products.html', context)
