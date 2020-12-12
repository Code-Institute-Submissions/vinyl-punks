from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Album
from django.http import JsonResponse


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    added_item = request.session.get('added_item', {})
    added_item = get_object_or_404(Album, pk=added_item)

    for item_id, quantity in cart.items():
        product = get_object_or_404(Album, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'added_item': added_item,
    }

    costs = {
        'delivery': delivery,
        'grand_total': grand_total,
        'total': total,
        'product_count': product_count,
    }

    if 'ajax' in request.GET:
        return JsonResponse(costs)

    return context
