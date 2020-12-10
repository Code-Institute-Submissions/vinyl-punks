from django.urls import path
from . import views
from cart import contexts
from cart.contexts import cart_contents

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_details, name='product_details'),
    path('delete_from_cart/<item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('cart_contents/', contexts.cart_contents, name='cart_contents'),
]
