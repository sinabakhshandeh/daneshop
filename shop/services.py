from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from shop.models import Product, ProductCategory


def get_products_list(category_slug) -> QuerySet:
    products = Product.objects.all().filter(status="published")
    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        products = products.filter(category=category)
    return products


def get_product_details(product_slug: str) -> Product:
    product = get_object_or_404(
        Product,
        status="published",
        slug=product_slug,
    )
    return product


def get_categories_list():
    categories = ProductCategory.objects.all()
    return categories
