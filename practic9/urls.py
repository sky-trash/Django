from django.urls import path
from .views import get_book_detail, get_books
urlpatterns = [
    path('', get_books),
    path('book/<int:pk>', get_book_detail, name='book_detail')
]
