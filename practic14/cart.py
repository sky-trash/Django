from typing import Any
from django.contrib.sessions.backends.base import SessionBase
from practic7.models import Product
from collections.abc import Iterator

class CartSession(SessionBase):
    CART_SESSION_ID = 'cart'

    def __init__(self, session:dict) -> None:
        self.session: dict = session
        self.cart = self.session.get(self.CART_SESSION_ID)

        if not self.cart:
            self.cart = self.session[self.CART_SESSION_ID] = {}

    def __iter__(self) -> Iterator[str]:
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session.modified = True

    def add(self, product:Product, quantity = 1, update_quantity= False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': product.price,
                'product': {
                    'id': product.id,
                    'title': product.title,
                    'rating': product.rating,
                    'price': product.price,
                    'image':product.image.url,
                }
            }

        if update_quantity: 
            self.cart[product_id]['quantity'] = quantity

        else: 
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product:Product):
        product_id = str(product.id)

        if product_id in self.cart:
            if self.cart[product_id]['quantity'] > 1:
                self.cart[product_id]['quantity'] -= 1
            else:
                del self.cart[product_id]
            self.save()

    def get_total_price(self): 
        return sum(int(item['price']) * int(item['quantity']) for item in self.cart.values())
    
    def clear(self):
        del self.session[self.CART_SESSION_ID]
        self.save()
