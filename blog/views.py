from django.shortcuts import render

from blog import services


def post_list_view(request):
    page = request.GET.get("page", 1)

    posts = services.post_list_view(page=page)
    context = {"posts": posts}
    return render(request, "blog/post_list_view.html", context)
