from django.shortcuts import redirect, render
from django.db.models import Q
from practic7.models import Product
from django.http import HttpRequest

def search_product(req: HttpRequest):
    if req.method == "GET":
        if (req.GET.get('search') is not None):
            search = req.GET.get('search')
            products = Product.objects.filter(
                Q(title__icontains = search)) 
            
            return render(req, template_name="practic10_search.html", context={
                'products': products,
            })
        else:
            return redirect('main')    
    return redirect('main')