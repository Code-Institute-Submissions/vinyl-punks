from django.urls import path
from . import views
from cart import contexts
from cart.contexts import cart_contents

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_details, name='product_details'),
    path('delete_from_cart/<item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('cart_contents/', contexts.cart_contents, name='cart_contents'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('update_review/<int:product_id>/', views.update_review, name='update_review'),
    path('add_tracks/', views.add_tracks, name='add_tracks'),
    path('delete_track/<int:track_id>/', views.delete_track, name='delete_track'),
]
