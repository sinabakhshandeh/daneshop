from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from shop.models import Product, ProductCategory


def get_products_list(category_slug: str, page_number: int) -> QuerySet:
    page_size = 8
    products = Product.objects.all().filter(status="published")
    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, page_size)
    try:
        products = paginator.get_page(page_number)
    except EmptyPage:
        products = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        products = paginator.get_page(1)
    return products


def get_product_details(product_slug: str) -> Product:
    product = get_object_or_404(
        Product,
        status="published",
        slug=product_slug,
    )
    return product


def get_categories_list() -> QuerySet:
    categories = ProductCategory.objects.all()
    return categories
