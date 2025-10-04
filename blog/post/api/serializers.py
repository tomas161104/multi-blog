from rest_framework import serializers
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer
from post.models import Posts
from blogs.api.serializers import BlogsSerializers

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    blogs = BlogsSerializers()
    class Meta:
        model = Posts
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'blogs', 'category']