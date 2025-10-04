from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from follows.models import Follow
from .serializers import FollowSerializer

class FollowApiViewSet(ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]