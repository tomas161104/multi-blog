from rest_framework import serializers
from comments.models import Comment
from users.api.serializers import UserSerializer
from post.api.serializers import PostSerializer


class CommentSerilizer(serializers.ModelSerializer):
    user = UserSerializer()
    posts = PostSerializer()
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'user', 'posts', 'image']