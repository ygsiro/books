from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('<str:book_id>', views.detail_book, name='detail_books'),
]