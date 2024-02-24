from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from blog.models import Post


def paginate(query_set: QuerySet, page: int):
    paginator = Paginator(query_set, 10)
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        query_set = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        query_set = paginator.page(paginator.num_pages)
    return query_set


def post_list_view(slug: str, page: int) -> QuerySet:
    categories = None
    posts = Post.objects.filter(status="published")
    if slug:
        posts = Post.objects.filter(category__slug=slug)
        categories = posts.first().category.get_ancestors()
    posts = paginate(query_set=posts, page=page)
    return posts, categories


def post_details_view(slug: str) -> QuerySet:
    post = get_object_or_404(Post, slug=slug)
    categories = post.category.get_ancestors()
    return post, categories
