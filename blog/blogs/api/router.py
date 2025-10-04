from rest_framework.routers import DefaultRouter
from .views import BlogApiSetView

router_blogs = DefaultRouter()

router_blogs.register(prefix='blogs', basename='blogs', viewset=BlogApiSetView)