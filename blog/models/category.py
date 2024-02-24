from typing import List

from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from daneshop.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default="")

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_ancestors(self) -> List:
        ancestors: list = [self]
        category = self
        while category.parent is not None:
            ancestors.insert(0, category.parent)
            category = category.parent
        return ancestors

    def get_absolute_url(self):
        return reverse(
            "blog:category_post_list",
            kwargs={"category_slug": self.slug},
        )
