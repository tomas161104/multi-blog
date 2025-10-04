from rest_framework.viewsets import ModelViewSet
from blogs.api.permission import IsOwnerOrReadOnly
from .serializers import BlogsSerializers
from blogs.models import Blogs

class BlogApiSetView(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BlogsSerializers
    queryset = Blogs.objects.all()