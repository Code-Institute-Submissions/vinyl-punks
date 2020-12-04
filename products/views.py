from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Album, Track


def all_products(request):
    """ A view to display all albums """

    albums = Album.objects.all()
    tracks = Track.objects.all()

    context = {
        'albums': albums,
        'tracks': tracks,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to display product details """

    album = get_object_or_404(Album, pk=product_id)
    tracks = Track.objects.filter(album=album)
    print(tracks)

    context = {
        'album': album,
        'tracks': tracks,
    }

    return render(request, 'products/product_details.html', context)
