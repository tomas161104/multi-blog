from django.db import models
from django.db.models import CASCADE
from users.models import User
from post.models import Posts
# Create your models here.

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    post = models.ForeignKey(Posts, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
