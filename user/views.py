from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import TemplateView, CreateView
from django.db.models import Count
from product.models import Book,Category
from order.models import OrderItem
# Create your views here.

class MainPage(TemplateView):
    template_name = 'user/index.html'
    orders = OrderItem.objects.values('product').annotate(count=Count('quantity')).order_by('-count')[:7]
    book = Book.objects.none()
    for order in orders:
        books = Book.objects.all().filter(id=order['product'])
        book |= books
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
