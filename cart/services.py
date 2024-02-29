from django.shortcuts import get_object_or_404

from cart.models import Cart


def get_cart_details(cart_uuid: str):
    cart = get_object_or_404(Cart, uuid=cart_uuid)
    return cart


def get_cart_items(cart_uuid: str):
    cart = get_object_or_404(Cart, uuid=cart_uuid)
    return cart.items.all()
