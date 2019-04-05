from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from orders.models import OrderItem
from orders.services import Cart
from products.models import Book, Category


class MainPage(TemplateView):
    template_name = 'user/index.html'
    book = Book.objects.none()
    categories = Category.objects.all()
    try:
        orders = OrderItem.objects.values('product').annotate(count=Count('quantity')).order_by('-count')
        for order in orders:
            print (orders)
            books = Book.objects.all().filter(id=order['product'])
            book |= books
    finally:
        pass

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data()
        cart = Cart(self.request)
        total_price = cart.get_total_price()
        total_items = cart.__len__()
        context['books'] = self.book
        context['categories'] = self.categories
        context['total_items'] = total_items
        context['total_price'] = total_price
        return context


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
