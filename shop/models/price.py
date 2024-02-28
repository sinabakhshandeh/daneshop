from django.db import models

from daneshop.models import BaseModel


class ProductPrice(BaseModel):
    product = models.ForeignKey(
        "Product", related_name="prices", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField()

    class Meta:
        verbose_name = "Product Price"
        verbose_name_plural = "Product Prices"
        ordering = ("effective_date",)

    def __str__(self):
        return f"{self.product.title} - {self.price} - {self.effective_date}"
