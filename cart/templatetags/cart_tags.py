from django import template

from cart.models import Cart, CartItem

register = template.Library()


@register.simple_tag
def cart_items_count(cart_uuid: str):
    cart = Cart.objects.get(uuid=cart_uuid)
    return CartItem.objects.all().filter(cart=cart).count()


@register.simple_tag
def cart_total_price(cart_uuid: str):
    cart = Cart.objects.get(uuid=cart_uuid)
    items = CartItem.objects.all().filter(cart=cart)
    prices = (item.total_price() for item in items)
    return sum(prices)
