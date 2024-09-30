from django.contrib import admin
from .models import pr8_product

@admin.register(pr8_product)
class AdminProduc(admin.ModelAdmin):
    pass 
