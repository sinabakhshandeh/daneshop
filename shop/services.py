from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from shop.models import Product, ProductCategory


def get_products_list() -> QuerySet:
    products = Product.objects.all().filter(status="published")
    return products


def get_product_details(product_slug: str) -> Product:
    product = get_object_or_404(
        Product,
        status="published",
        slug=product_slug,
    )
    return product


def get_categories_list():
    categories = ProductCategory.objects.all().filter(status="published")
    return categories
