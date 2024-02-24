from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Category, Comment, CommentReply, Post


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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Comment
        fields = ["text", "timestamp", "author", "replies"]

    def get_replies(self, instance):
        replies = instance.replies.all()
        return ReplySerializer(replies, many=True).data

    def to_representation(self, instance: Post):
        representation = super().to_representation(instance)
        representation["author"] = instance.author.username
        return representation


class ReplySerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = CommentReply
        fields = ["text", "timestamp", "author"]

    def to_representation(self, instance: Post):
        representation = super().to_representation(instance)
        representation["author"] = instance.author.username
        return representation
