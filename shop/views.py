from django.shortcuts import render

from shop import services


def shop_product_list_view(request):
    products = services.get_products_list()
    context = {"products": products}
    return render(request, "shop/pages/main.html", context)
