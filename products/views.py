from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponse
from .models import Album, Track, Genre, Review
from .forms import ProductForm, ReviewForm
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
    reviews = Review.objects.filter(album=album)
    form = ReviewForm()

    context = {
        'album': album,
        'tracks': tracks,
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'You do not have the rights to execute this task.')
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


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'You do not have the rights to execute this task.')
        return redirect(reverse('products'))

    product = get_object_or_404(Album, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please make sure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'You do not have the rights to execute this task.')
        return redirect(reverse('products'))

    product = get_object_or_404(Album, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """Add a product to the store"""

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.album = Album(pk=product_id)
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_details', args=[product_id]))
        else:
            messages.error(request, 'Failed to add review. Please ensure the form is valid.')

    return redirect(reverse('product_details', args=[product_id]))


@login_required
@require_POST
def update_review(request, product_id):
    """ Edit a review with AJAX """

    try:
        updated_review = request.POST['content']
        review = get_object_or_404(Review, pk=product_id)
        if review.author == request.user:
            review.content = updated_review
            review.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=403)

    except Exception as e:
        return HttpResponse(content=e, status=403)


def add_tracks(request):
    """ Add tracks to albums """
    albums = Album.objects.all()
    post_items = list(request.POST.items())
    if request.method == 'POST':
        album = request.POST['album']
        for track, title in post_items[2:]:
            track = Track(title=title, album=Album(id=album))
            track.save()

        return redirect(reverse('product_details', args=[album]))

    context = {
        'albums': albums,
    }

    return render(request, 'products/add_tracks.html', context)


def delete_track(request, track_id):
    """Delete a track from album"""
    if not request.user.is_superuser:
        messages.error(request, 'You do not have the rights to execute this task.')
        return redirect(reverse('products'))

    track = get_object_or_404(Track, pk=track_id)
    album = get_object_or_404(Album, title=track.album)
    track.delete()
    messages.success(request, 'Track deleted!')
    return redirect(reverse('product_details', args=[album.id]))
