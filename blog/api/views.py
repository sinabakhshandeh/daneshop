from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog import services
from blog.api.serializers import PostSerializer


@api_view(["GET"])
def post_list_api(request):
    posts, categories = services.post_list_view(slug="", page=1)
    serialize = PostSerializer(instance=posts, many=True)
    return Response(serialize.data)


@api_view(["GET"])
def post_details_view_api(request, post_slug: str):
    post, categories = services.post_details_view(slug=post_slug)
    serialize = PostSerializer(instance=post)
    return Response(serialize.data)
