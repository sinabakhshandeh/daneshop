import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from daneshop.models import BaseModel
from shop.models import Product


class Cart(BaseModel):
    class CartStatus(models.TextChoices):
        PAID = "paid", _("PAID")
        NOT_PAID = "not_paid", _("NO_TPAID")

    cart_status = models.CharField(
        max_length=25,
        choices=CartStatus.choices,
        default=CartStatus.NOT_PAID,
        help_text=_("Status"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="carts",
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def is_defined(self, product: Product):
        item = CartItem.objects.filter(cart=self, product=product)
        if item.exists():
            return True
        else:
            return False

    def get_absolute_url(self):
        return reverse("cart:cart_details", kwargs={"cart_uuid": self.uuid})


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
