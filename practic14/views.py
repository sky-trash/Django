from django.shortcuts import render,redirect, get_object_or_404
from .cart import CartSession
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from practic7.models import Product
from .forms import OrderForm
from practic15.models import OrderItem, Order

def cart_add(req: HttpRequest, product_id):
    cart = CartSession(req.session)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

def cart_remove(req:HttpRequest, product_id):
    cart = CartSession(req.session)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect('cart_detail')

def cart_remove_all(req:HttpRequest): 
    cart = CartSession(req.session)
    cart.clear()
    return redirect('cart_detail')

@login_required(login_url='login')
def cart_detail(req: HttpRequest):
    cart = CartSession(req.session)
    if req.method == 'POST':
        form = OrderForm(req.POST)
        if form.is_valid():
            order = Order.objects.create(customer_user=req.user, customer_email=form.data.get('customer_email'), )
            for item_cart in cart:
                 OrderItem.objects.create(order=order, product=item_cart['product'], quantity=item_cart['quantity']).save()
            cart.clear()
            return redirect('profile')
    else:
        form = OrderForm()
        return render(req, 'practic14_cart_detail.html', {
            'form': form,
            'cart':cart
        })


