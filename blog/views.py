from django.shortcuts import render

from blog import services


def post_list_view(request):
    posts = services.post_list_view()
    context = {"posts": posts}
    return render(request, "blog/post_list_view.html", context)
