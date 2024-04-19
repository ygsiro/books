from django.http import HttpResponse
from django.template import loader
from .models import Book

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {
        'title': 'List Books',
        'books': books
    }
    template = loader.get_template('books/list_books.html')
    return HttpResponse(template.render(context, request))

def detail_book(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
    except Book.DoesNotExist:
        book = None

    context = {
        'title': 'Detail Book',
        'book': book,
    }
    template = loader.get_template('books/detail_book.html')
    return HttpResponse(template.render(context, request))