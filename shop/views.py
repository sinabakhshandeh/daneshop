from django.shortcuts import render

from shop import services


def shop_product_list_view(request, category_slug: str = ""):
    page_number = request.GET.get("page", 1)
    products = services.get_products_list(category_slug, page_number)
    context = {"products": products}
    return render(request, "shop/pages/main.html", context)


def shop_product_details_view(request, product_slug: str):
    product = services.get_product_details(product_slug=product_slug)
    context = {"product": product}
    return render(request, "shop/pages/product.html", context)


def shop_category_list_view(request):
    categories = services.get_categories_list()
    context = {"categories": categories}
    return render(request, "shop/pages/categories.html", context)
