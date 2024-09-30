from django.urls import path
from practic8.views import index

urlpatterns = [
    path('', index, name="home")
]