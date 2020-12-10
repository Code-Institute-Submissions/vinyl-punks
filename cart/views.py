from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Album


def view_cart(request):
    """ A view that renders the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of thye product to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

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
