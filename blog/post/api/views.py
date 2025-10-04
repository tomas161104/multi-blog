from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from blogs.api.permission import IsOwnerOrReadOnly
from post.models import Posts
from .serializers import PostSerializer


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Posts.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug']
