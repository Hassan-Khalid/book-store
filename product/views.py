from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Category, Book
from django.views.generic import DetailView, TemplateView, ListView


# Create your views here.


class BookListView(ListView):
    template_name = "books.html"
    books = Book.objects.all()
    model = Book
    categories = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = {
            'categories': self.categories,
            'books': self.books
        }
        return context


def search_book(request):
    category = Category.objects.all()
    if request.POST:
        book_name_to_search = request.POST.get('book-search')
        book_name_to_search=book_name_to_search.lower()
        books = Book.objects.filter(name__iregex=r"(^|\s)%s" % book_name_to_search)
        print(books)
        context = {
            'books': books,
            'category':category
        }
        return render(request,'books.html',context)
    else:
        context={
            'category':category
        }
        return render(request,'books.html',context)


def top_seller_book(request):
    # books = get_object_or_404(Book, category_id=id, slug=slug)
    books = Book.objects.filter()
    context = {
        'books': books,
    }
    return render(request, 'index.html', context)


def book_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    books = Book.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        books = Book.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'books': books
    }
    return render(request, 'book-category.html', context)
