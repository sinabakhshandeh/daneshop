from django import template

from shop.models.category import ProductCategory
from shop.models.product import Product

register = template.Library()


@register.inclusion_tag("shop/component/related.html")
def related_products(slug, category: str):
    category = ProductCategory.objects.get(
        slug=category,
    )
    produts = Product.objects.filter(
        category=category,
        status="published",
    ).exclude(slug=slug)

    return {"products": produts[:4]}
