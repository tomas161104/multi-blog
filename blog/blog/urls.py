"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from categories.api.router import router_categories
from post.api.router import router_posts
from comments.api.router import router_comment
from blogs.api.router import router_blogs
from follows.api.router import router_follows
from likes.api.router import router_like

schema_view = get_schema_view(
   openapi.Info(
      title="blog API",
      default_version='v1',
      description="blog Project",
      terms_of_service="",
      contact=openapi.Contact(email="tomastrigal680@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('users.api.router')),
    path('api/', include(router_categories.urls)),
    path('api/', include(router_posts.urls)),
    path('api/', include(router_comment.urls)),
    path('api/', include(router_blogs.urls)),
    path('api/', include(router_follows.urls)),
    path('api/', include(router_like.urls))
]
