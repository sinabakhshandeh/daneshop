from django.http import Http404
from django.shortcuts import render

from blog import services


def post_list_view(request, category_slug: str = ""):
    page = request.GET.get("page", 1)
    posts, categories = services.post_list_view(
        slug=category_slug,
        page=page,
    )
    context = {"posts": posts, "categories": categories}
    return render(request, "blog/post_list_view.html", context)


def post_details_view(request, post_slug: str):
    try:
        post, categories = services.post_details_view(slug=post_slug)
    except Exception:
        raise Http404("Post not found")

    context = {"post": post, "categories": categories}
    return render(request, "blog/post_details_view.html", context)
