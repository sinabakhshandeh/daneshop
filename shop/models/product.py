from django.db import models
from django.db.models import JSONField

from daneshop.models import BaseModel

from .category import ProductCategory
from .price import ProductPrice


class Product(BaseModel):
    category = models.ForeignKey(
        ProductCategory, related_name="products", on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    attributes = JSONField(blank=True, null=True)

    @property
    def last_price(self):
        return ProductPrice.objects.all().filter(product=self).last()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("created_at",)

    def __str__(self):
        return self.title
