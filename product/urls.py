from django.conf.urls import url
from django.urls import path

from .views import BookListView, top_seller_book, book_list

app_name = 'product'

urlpatterns = [
    path("books/", BookListView.as_view(), name='books'),
    url(r'^(?P<category_slug>[-\w]+)/$', book_list, name='book-list'),

]
