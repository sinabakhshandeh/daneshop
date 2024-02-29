from django import template
from django.contrib.auth.models import User

from cart.models import Cart, CartItem

register = template.Library()


@register.simple_tag
def cart_items_count(cart_uuid: str):
    print(cart_uuid)
    cart = Cart.objects.get(uuid=cart_uuid)
    return CartItem.objects.all().filter(cart=cart).count()


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
            status="not_paid",
        )
        if carts.exists():
            return carts.last().uuid
        else:
            cart = Cart.objects.create(
                user=user,
                status="not_paid",
            )
            return cart.uuid
    return False
