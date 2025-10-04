from django.db.models import CASCADE
from django.db import models
from users.models import User
from categories.models import Categorie

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=CASCADE)
    category = models.ForeignKey(Categorie, on_delete=CASCADE)
    