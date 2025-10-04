from rest_framework.routers import DefaultRouter
from .views import LikeApiViewSet

router_like = DefaultRouter()

router_like.register(prefix='likes', basename='likes', viewset=LikeApiViewSet)