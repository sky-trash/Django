from django.urls import path
from practic2.views import hello 

urlpatterns = [
    path('library/', hello),
]