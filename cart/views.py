from django.shortcuts import render

from cart import services


def cart_details(request, cart_uuid: str):
    cart = services.get_cart_details(cart_uuid)
    items = services.get_cart_items(cart_uuid)
    context = {"cart": cart, "items": items}
    return render(request, "cart/pages/cart.html", context)
