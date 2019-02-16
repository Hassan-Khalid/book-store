from django.urls import path

from .views import BookListView, book_list, search_book

app_name = 'products'

urlpatterns = [
    path("books/", BookListView.as_view(), name='books'),
    path("<category_slug>", book_list, name='book-list'),
    path("books/search", search_book, name='search_book'),

]
