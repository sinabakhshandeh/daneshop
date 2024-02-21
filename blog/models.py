import uuid
from typing import List

from django.contrib.auth.models import User
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


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class CommentReply(models.Model):
    comment = models.ForeignKey(
        "Comment", on_delete=models.CASCADE, related_name="replies"
    )
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text
