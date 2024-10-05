from rest_framework import serializers
from .models import Blog
from user_authentication.models import CustomUser


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model to represent the author of a blog
    """

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"]


class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for the Blog model, including author details
    """

    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "short_description",
            "content",
            "image",
            "author",
            "created_at",
        ]
        read_only_fields = ["id", "created_at", "author"]


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model to handle user profile information
    """

    class Meta:
        model = CustomUser
        fields = ["username", "email", "profile_picture"]
