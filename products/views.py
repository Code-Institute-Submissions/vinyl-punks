from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Album, Track
from django.db.models import Q


def all_products(request):
    """ A view to display all albums """
    query = None

    albums = Album.objects.all()
    tracks = Track.objects.all()

    if request.GET:
        if 'search_query' in request.GET:
            query = request.GET['search_query']
            if not query:
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(artist__icontains=query)
            albums = albums.filter(queries)

    context = {
        'albums': albums,
        'tracks': tracks,
        'query': query
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to display product details """

    album = get_object_or_404(Album, pk=product_id)
    tracks = Track.objects.filter(album=album)

    context = {
        'album': album,
        'tracks': tracks,
    }

    return render(request, 'products/product_details.html', context)
