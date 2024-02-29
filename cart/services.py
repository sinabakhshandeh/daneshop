from django.shortcuts import get_object_or_404

from cart.models import Cart, CartItem
from shop.services import get_product_details


def get_cart_details(cart_uuid: str):
    cart = get_object_or_404(Cart, uuid=cart_uuid)
    return cart


def get_cart_items(cart_uuid: str):
    cart = get_cart_details(cart_uuid=cart_uuid)
    return cart.items.all()


def add_item(request, product_slug: str, quantity: int):
    user = request.user
    carts = Cart.objects.filter(user=user, cart_status="not_paid")
    product = get_product_details(product_slug)

    if not carts.exists():
        cart = Cart.objects.create(user=user)
    else:
        cart = carts.last()

    if not cart.is_defined(product=product):
        CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=quantity,
        )
    else:
        item = CartItem.objects.filter(
            cart=cart,
            product=product,
        ).last()
        item.quantity += quantity
        item.save()

    return {"message": "success"}


def pay(request):
    user = request.user
    cart = Cart.objects.filter(user=user, cart_status="not_paid").last()
    cart.cart_status = "paid"
    cart.save()
