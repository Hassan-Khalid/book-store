from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Book

from .forms import OrderCreateForm, CartAddProductForm
from .models import OrderItem, Order
from .services import Cart


@login_required
def order_create(request):
    cart = Cart(request)
    order = Order.objects.none()
    if request.method == 'POST':
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

        return render(request, 'thanks.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'order.html', {'form': form, 'cart': cart})


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(book_id, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('orders:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart_detail.html', {'cart': cart})


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=product_id)
    cart.remove(product)
    return redirect('orders:cart_detail')
