from rest_framework import serializers
from categories.models import Categorie


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['title', 'slug', 'published']