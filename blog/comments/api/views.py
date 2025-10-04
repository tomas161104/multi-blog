from rest_framework.viewsets import ModelViewSet
from categories.api.permissions import IsAdminOrReadOnly
from .serializers import CommentSerilizer
from comments.models import Comment

class CommentApiViewSet(ModelViewSet):
    serializer_class = CommentSerilizer
    queryset = Comment.objects.all()
    permission_classes = [IsAdminOrReadOnly]