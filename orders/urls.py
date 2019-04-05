from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path("", views.CartDetails.as_view(), name='cart_detail'),
    path('create', views.CreateOrder.as_view(), name='order'),
    path('thanks', views.OrderCompleted.as_view(), name='complete'),
    path("add/<book_id>", views.CartAddItem.as_view(), name='cart_add'),
    path("remove/<int:product_id>", views.RemoveProductFromCart.as_view(), name='cart_remove'),
]
