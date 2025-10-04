from django.db import models
from django.db.models import CASCADE, SET_NULL
from users.models import User
from blogs.models import Blogs

# Create your models here.
class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('user', 'blog')