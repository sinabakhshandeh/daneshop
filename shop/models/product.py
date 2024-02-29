from django.db import models
from django.db.models import JSONField
from django.urls import reverse

from daneshop.models import BaseModel

from .category import ProductCategory
from .media import ProductMedia
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

    @property
    def get_media(self):
        return (
            ProductMedia.objects.all()
            .filter(
                product=self,
                file_type="image",
            )
            .first()
        )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("created_at",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "shop:product_details",
            kwargs={"product_slug": self.slug},
        )
