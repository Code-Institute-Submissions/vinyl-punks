from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Album, Track, Genre
from django.db.models import Q
from django.db.models.functions import Lower


def all_products(request):
    """ A view to display all albums """
    query = None
    genre = None
    era = None
    special_edition = False
    sort = None
    direction = None
    albums = Album.objects.all()
    tracks = Track.objects.all()

    if request.GET:

        if 'genre' in request.GET:
            genre = request.GET['genre']
            albums = albums.filter(genre__name=genre)

        if 'era' in request.GET:
            era = request.GET['era']
            albums = albums.filter(era=era)

        if 'special_edition' in request.GET:
            special_edition = request.GET['special_edition']
            albums = albums.filter(special_edition=special_edition)

        if 'search_query' in request.GET:
            query = request.GET['search_query']
            if not query:
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(artist__icontains=query)
            albums = albums.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            albums = albums.order_by(sortkey)

    context = {
        'albums': albums,
        'tracks': tracks,
        'query': query,
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
