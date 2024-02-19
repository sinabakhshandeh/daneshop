from django.http import Http404
from django.shortcuts import render

from blog import services


def post_list_view(request):
    page = request.GET.get("page", 1)
    posts = services.post_list_view(page=page)

    context = {"posts": posts}
    return render(request, "blog/post_list_view.html", context)


def post_details_view(request, post_slug: str):
    try:
        post = services.post_details_view(slug=post_slug)
    except Exception:
        raise Http404("Post not found")
    categories = post.category.get_ancestors()

    context = {"post": post, "categories": categories}
    return render(request, "blog/post_details_view.html", context)
