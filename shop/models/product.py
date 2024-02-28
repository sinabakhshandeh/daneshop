from django.db import models
from django.db.models import JSONField

from daneshop.models import BaseModel

from .category import ProductCategory


class Product(BaseModel):
    category = models.ForeignKey(
        ProductCategory, related_name="products", on_delete=models.CASCADE
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    attributes = JSONField(blank=True, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("created_at",)

    def __str__(self):
        return self.title
