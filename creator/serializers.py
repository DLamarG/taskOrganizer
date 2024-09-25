from rest_framework import serializers
from . import models
# from main.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields=['my_task', 'user']