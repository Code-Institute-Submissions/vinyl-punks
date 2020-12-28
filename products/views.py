from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Album, Track, Genre
from .forms import ProductForm
from django.db.models import Q
from cart.views import delete_from_cart


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


def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('products'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
