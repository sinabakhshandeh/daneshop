from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Category, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
    )

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
            "category",
        ]

    def to_representation(self, instance: Post):
        representation = super().to_representation(instance)
        representation["author"] = instance.author.username

        categories = instance.category.get_ancestors()
        categories.reverse()
        representation["categories"] = CategorySerializer(
            categories,
            many=True,
        ).data
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
