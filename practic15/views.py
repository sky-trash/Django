from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from .models import OrderItem, Order
from practic14.forms import OrderForm
from practic14.cart import CartSession

@login_required(login_url='login')
def create_order(req: HttpRequest):
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
            'form': form
        })