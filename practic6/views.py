from django.shortcuts import render
from practic4.models import Book

def get_info(req):
    book = Book.objects.get(id=1)
    return render(req, 'practic6_index.html', context ={
        'book':book
    })
    
def get_author(req):
    book_author = Book.objects.filter(author__name='Матвеев Евгений Игоревич')
    return render(req, 'practic6_author.html', context ={
        'book_author':book_author
    })

def get_author_task(req):
    book_author = Book.objects.filter(author__name='Путин Владимир Владимирович')
    return render(req, 'practic6_author.html', context ={
        'book_author':book_author
    })

def get_author_taskPublisher(req):
    book_publisher = Book.objects.filter(publishers__name='Издание №1')
    return render(req, 'practic6_author.html', context ={
        'book_author':book_publisher
    })