from django.shortcuts import render


def all_products(request):
    """ A view to display all products """

    return render(request, 'products/products.html')
