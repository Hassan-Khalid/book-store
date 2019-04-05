from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView
from orders.services import Cart

from .models import Category, Book


class BookListView(ListView):
    template_name = "books.html"
    books = Book.objects.all()
    model = Book
    categories = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data()
        cart = Cart(self.request)
        total_items = cart.__len__()
        total_price = cart.get_total_price()

        context['books'] = self.books
        context['categories'] = self.categories
        context['total_items'] = total_items
        context['total_price'] = total_price
        return context


class SearchBook(TemplateView):
    template_name = 'book-category.html'
    categories = Category.objects.all()
    books = Book.objects.none()

    def post(self, request):
        book_name_to_search = request.POST.get('book-search')
        book_name_to_search = book_name_to_search.lower()
        self.books = Book.objects.filter(name__iregex=r"(^|\s)%s" % book_name_to_search)
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self):
        context = super(SearchBook, self).get_context_data()
        cart = Cart(self.request)
        total_price = cart.get_total_price()
        total_items = cart.__len__()
        context['books'] = self.books
        context['categories'] = self.categories
        context['total_items'] = total_items
        context['total_price'] = total_price
        return context


class BookListByCategory(TemplateView):
    template_name = 'book-category.html'

    def get_context_data(self, category_slug=None, **kwargs):
        context = super(BookListByCategory, self).get_context_data()
        categories = Category.objects.all()
        books = Book.objects.all()
        cart = Cart(self.request)
        total_items = cart.__len__()
        total_price = cart.get_total_price()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            books = Book.objects.filter(category=category)
        context['categories'] = categories
        context['books'] = books
        context['total_price'] = total_price
        context['total_items'] = total_items

        return context
