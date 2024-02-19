from django.db import models

from blog.models import Post


def post_list_view() -> models.QuerySet:
    posts = Post.objects.filter(status="published")
    return posts
