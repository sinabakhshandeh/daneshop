from django.db.models import QuerySet

from shop.models import Product


def get_products_list() -> QuerySet:
    products = Product.objects.all().filter(status="published")
    return products
