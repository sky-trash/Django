from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Product
from django.http import HttpRequest

def main(req):
    return render(req, 'practic7_index.html')

def about(req):
    return render(req, 'practic7_about.html')

def products(req):
    products = Product.objects.all()
    return render(req, 'practic7_products.html', context ={
        'products': products
    })

def get_product_detail(req, pk):
    productDetail = Product.objects.get(pk = pk)
    return render(req, 'practic7_productPage.html', context = {
        'productDetail':productDetail
    })
    