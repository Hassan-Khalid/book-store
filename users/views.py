from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from orders.models import OrderItem
from products.models import Book, Category


# Create your views here.

class MainPage(TemplateView):
    template_name = 'user/index.html'
    book = Book.objects.none()
    try:
        orders = OrderItem.objects.values('product').annotate(count=Count('quantity')).order_by('-count')[:7]
        for order in orders:
            books = Book.objects.all().filter(id=order['product'])
            book |= books
    finally:
        pass

    categories = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = {
            'categories': self.categories,
            'books': self.book
        }
        return context


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
