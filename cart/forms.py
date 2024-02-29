from django import forms


class CartItemForm(forms.Form):
    product_slug = forms.SlugField()
    quantity = forms.IntegerField()
