import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from daneshop.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    published_at = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-published_at",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_details", kwargs={"post_slug": self.slug})
