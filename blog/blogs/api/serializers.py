from rest_framework import serializers
from blogs.models import Blogs
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

class BlogsSerializers(serializers.ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer
    class Meta:
        model = Blogs
        fields = ['id', 'title', 'desc', 'created_at', 'owner', 'category']