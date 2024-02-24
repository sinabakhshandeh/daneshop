from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog import services
from blog.api.serializers import PostSerializer


@api_view(["GET"])
def post_list_api(request):
    posts, categories = services.post_list_view(slug="", page=1)
    serialize = PostSerializer(instance=posts, many=True)
    return Response(serialize.data)
