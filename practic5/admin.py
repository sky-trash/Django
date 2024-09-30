from django.contrib import admin
from practic4.models import Author, Book, Publisher

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    pass
@admin.register(Book)
class AdminAuthor(admin.ModelAdmin):
    pass
@admin.register(Publisher)
class AdminAuthor(admin.ModelAdmin):
    pass