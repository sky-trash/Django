from django.urls import path
from .views import cart_detail, cart_add, cart_remove, cart_remove_all

urlpatterns = [
    path('cart', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>', cart_remove, name='cart_remove'),
    path('cart/remove/all', cart_remove_all, name='cart_remove_all'),

    ]