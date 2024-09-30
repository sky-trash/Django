from django.urls import path
from practic1.views import hello 

urlpatterns = [
    path('', hello),
]