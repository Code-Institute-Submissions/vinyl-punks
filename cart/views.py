from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Album
from django.contrib import messages


def view_cart(request):
    """ A view that renders the cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the product to the cart """
    ADDED_TO_CART = 26  # Custom message level
    product = Album.objects.get(pk=item_id)
    # added_item = request.session.get('added_item', {})
    request.session['added_item'] = {}
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    redirect_url = request.POST.get('redirect_url')

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.add_message(request,
                             ADDED_TO_CART, f'Added another copy of '
                             f'{product.artist} - {product.title} '
                             f'to your cart')
    else:
        cart[item_id] = quantity
        messages.add_message(request, ADDED_TO_CART, f'Added {product.artist} '
                             f'- {product.title} to your cart')

    request.session['added_item'] = item_id
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update quantity of product """

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

    try:
        cart.pop(item_id)
        request.session['cart'] = cart
        if 'ajax' in request.GET:
            return HttpResponse(status=200)
        else:
            return redirect(reverse('view_cart'))
    except Exception as e:
        if 'ajax' in request.GET:
            return HttpResponse(content=e, status=500)
        else:
            messages.error(request, f'Something went wrong: {e}')
            return redirect(reverse('view_cart'))
