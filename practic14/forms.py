from django import forms  
from practic15.models import Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_email']