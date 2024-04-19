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