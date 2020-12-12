from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Album
from django.contrib import messages


def view_cart(request):
    """ A view that renders the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the product to the cart """
    product = Album.objects.get(pk=item_id)
    added_item = request.session.get('added_item', {})
    request.session['added_item'] = {}
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    redirect_url = request.POST.get('redirect_url')

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Added another copy of {product.artist} - {product.title} to your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.artist} - {product.title} to your cart')

    request.session['added_item'] = item_id
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update quantity of product """

    product = get_object_or_404(Album, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, item_id):
    """ Remove an item from the cart """

    cart = request.session.get('cart', {})

    cart.pop(item_id)
    request.session['cart'] = cart

    return redirect(reverse('view_cart'))
