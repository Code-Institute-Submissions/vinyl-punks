from django.urls import path
from . import views, contexts

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<item_id>/', views.update_cart, name='update_cart'),
    path('delete_from_cart/<item_id>/', views.delete_from_cart,
         name='delete_from_cart'),
    path('cart_contents/', contexts.cart_contents, name='cart_contents'),
]
