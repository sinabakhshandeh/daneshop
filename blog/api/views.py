from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog import services
from blog.api import serializers


@api_view(["GET"])
def post_list_api(request):
    posts, categories = services.post_list_view(slug="", page=1)
    serialize = serializers.PostSerializer(instance=posts, many=True)
    return Response(serialize.data)


@api_view(["GET"])
def post_details_view_api(request, post_slug: str):
    post, categories = services.post_details_view(slug=post_slug)
    post_serializer = serializers.PostSerializer(instance=post)
    category_serializer = serializers.CategorySerializer(
        instance=categories,
        many=True,
    )
    comments = post.comments.all()
    comment_serializer = serializers.CommentSerializer(
        instance=comments,
        many=True,
    )

    serialized_data = {
        "post": post_serializer.data,
        "categories": category_serializer.data,
        "comments": comment_serializer.data,
    }
    return Response(serialized_data)
