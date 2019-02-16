from django import forms

from .models import Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 5)]


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['email', 'address']


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
