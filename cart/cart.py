from decimal import Decimal
from django.conf import settings
from product.models import Book


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, book_id, quantity=1, update_quantity=False):
        book = Book.objects.get(id=book_id)
        book_ = str(book_id)
        print(book)
        if book_ not in self.cart:
            self.cart[book_] = {'quantity': 0, 'price': str(book.price), 'name': str(book.name), 'book_id': book_id}
        if update_quantity:
            self.cart[book_]['quantity'] = quantity
        else:
            self.cart[book_]['quantity'] += quantity

        print(self.cart)
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        for book in books:
            self.cart[str(book.id)]['book'] = book

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
