from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path("books/", views.BookListView.as_view(), name='books'),
    path("<category_slug>", views.BookListByCategory.as_view(), name='book-list'),
    path("books/search", views.SearchBook.as_view(), name='search_book'),

]
