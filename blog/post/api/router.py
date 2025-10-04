from rest_framework.routers import DefaultRouter
from .views import PostApiViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='posts', basename='posts', viewset=PostApiViewSet)