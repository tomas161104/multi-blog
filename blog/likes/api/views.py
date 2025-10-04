from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from likes.models import Like
from .serializer import LikeSerializer


class LikeApiViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]