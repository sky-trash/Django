from django.shortcuts import render
from practic4.models import Book

def get_book_detail(req, pk):
    bookDetail = Book.objects.get(pk = pk)
    return render(req, 'practic9_detail_book.html', context = {
        'bookDetail':bookDetail
    })
    
def get_books(req):
    books = Book.objects.all
    return render(req, 'practic9_main_page.html', context ={
        'books':books
    })
