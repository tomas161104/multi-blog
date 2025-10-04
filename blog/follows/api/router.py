from rest_framework.routers import DefaultRouter
from .views import FollowApiViewSet

router_follows = DefaultRouter()

router_follows.register(prefix='follows', basename='follows', viewset=FollowApiViewSet)