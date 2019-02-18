from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from products.models import Book

from .forms import OrderCreateForm, CartAddProductForm
from .models import OrderItem, Order
from .services import Cart


@method_decorator(login_required, name='dispatch')
class CreateOrder(TemplateView):
    template_name = 'order.html'

    def post(self, request):
        cart = Cart(request)
        order = Order.objects.none()
        form = OrderCreateForm(request.POST)
        user = request.user
        if form.is_valid():
            cd = form.cleaned_data
            order = Order.objects.create(
                user=user,
                email=cd['email'],
                address=cd['address']
            )
            order.save()
            for item in cart:
                q_book = (Book.objects.filter(id=item['book_id']))

                OrderItem.objects.create(
                    order=order,
                    product=q_book[0],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return HttpResponseRedirect('/orders/thanks', {'order': order})

    def get_context_data(self, *args):
        context = super(CreateOrder, self).get_context_data()
        form = OrderCreateForm()
        cart = Cart(self.request)
        total_items = cart.__len__()
        total_price = cart.get_total_price()
        context['cart'] = cart
        context['form'] = form
        context['total_items'] = total_items
        context['total_price'] = total_price
        print(total_items, total_price)
        return context


class OrderCompleted(TemplateView):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        context = super(OrderCompleted, self).get_context_data()
        context['order'] = Order.objects.latest('id')
        return context


@method_decorator(require_POST, name='dispatch')
class CartAddItem(TemplateView):
    def post(self, request, book_id, *args, **kwargs):
        cart = Cart(request)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(book_id, quantity=cd['quantity'], update_quantity=cd['update'])
        return HttpResponseRedirect('/orders/')


class CartDetails(TemplateView):
    template_name = 'cart_detail.html'

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
        context = {'cart': cart}
        return self.render_to_response(context)


class RemoveProductFromCart(TemplateView):
    template_name = 'cart_detail.html'

    def get(self, request, product_id, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Book, id=product_id)
        print(product)
        cart.remove(product)
        return HttpResponseRedirect('/orders/')
