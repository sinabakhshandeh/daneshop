from django import template

from cart.models import Cart, CartItem

register = template.Library()


@register.simple_tag
def cart_items_count(cart_uuid: str):
    cart = Cart.objects.get(uuid=cart_uuid)
    return CartItem.objects.all().filter(cart=cart).count()
