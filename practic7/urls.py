from django.urls import path
from practic7.views import main ,about,products,get_product_detail

urlpatterns = [
    path('', main, name="mainPage"),
    path('about/', about),
    path('products/', products),
    path('product/<int:pk>', get_product_detail, name='product_detail')
]