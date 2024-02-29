from django import template
from django.contrib.auth.models import User

from cart.models import Cart, CartItem

register = template.Library()


@register.simple_tag
def cart_items_count(cart_uuid: str):
    carts = Cart.objects.filter(uuid=cart_uuid, cart_status="not_paid")
    if carts.exists():
        return CartItem.objects.all().filter(cart=carts.last()).count()
    else:
        return 0


@register.simple_tag
def cart_total_price(cart_uuid: str):
    cart = Cart.objects.get(uuid=cart_uuid)
    items = CartItem.objects.all().filter(cart=cart)
    prices = (item.total_price() for item in items)
    return sum(prices)


@register.simple_tag
def has_cart(username: str):
    users = User.objects.filter(username=username)
    if users.exists():
        user = users.last()
        carts = Cart.objects.filter(
            user=user,
            cart_status="not_paid",
        )
        if carts.exists():
            return carts.last().uuid
        else:
            cart = Cart.objects.create(
                user=user,
                cart_status="not_paid",
            )
            return cart.uuid
    return False
