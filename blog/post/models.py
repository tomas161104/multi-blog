from django.db import models
from django.db.models import CASCADE, SET_NULL
from blogs.models import Blogs
from categories.models import Categorie

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)
    miniature = models.ImageField(upload_to='posts/img/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    blog = models.ForeignKey(Blogs, on_delete=CASCADE, null=True, blank=True)
    category = models.ForeignKey(Categorie, on_delete=SET_NULL, null=True)


    def __str__(self):
        return self.title
