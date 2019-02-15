from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from product.models import Book
from .cart import Cart
from django.core.serializers import serialize, get_serializer
from .forms import CartAddProductForm
from importlib import import_module
from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore


# Create your views here.
@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(book_id, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart_detail.html', {'cart': cart})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
