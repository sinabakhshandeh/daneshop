from django.contrib.auth.models import User
from django.db import models

from daneshop.models import BaseModel
from shop.models import Product


class Cart(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="carts",
    )

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(BaseModel):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} ({self.quantity}) in Cart"

    def total_price(self):
        return self.product.last_price.price * self.quantity
