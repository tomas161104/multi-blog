from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadOnly
from categories.models import Categorie

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Categorie.objects.filter(published=True)
    lookup_field = 'slug'