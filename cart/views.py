from django.shortcuts import HttpResponse, render

from cart import services
from cart.forms import CartItemForm


def cart_details(request, cart_uuid: str):
    cart = services.get_cart_details(cart_uuid)
    items = services.get_cart_items(cart_uuid)
    context = {"cart": cart, "items": items}
    return render(request, "cart/pages/cart.html", context)


def add_item(request):
    if request.method == "POST":
        form = CartItemForm(request.POST)
        if form.is_valid():
            product_slug = form.cleaned_data["product_slug"]
            quantity = form.cleaned_data["quantity"]
            services.add_item(request, product_slug, quantity)
            return HttpResponse("success")
    return HttpResponse("fail")
