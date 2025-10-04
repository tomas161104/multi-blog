from django.db import models
from django.db.models import CASCADE
from users.models import User
from post.models import Posts

# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    posts = models.ForeignKey(Posts, on_delete=CASCADE)
    image = models.ImageField(upload_to='comments/img/')