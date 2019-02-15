from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from product.models import Book


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
