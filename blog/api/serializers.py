from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = [
            "status",
            "title",
            "content",
            "published_at",
            "slug",
            "uuid",
            "author",
        ]

    def to_representation(self, instance: Post):
        representation = super().to_representation(instance)
        representation["author"] = instance.author.username
        return representation
