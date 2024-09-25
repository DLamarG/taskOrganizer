from rest_framework import serializers
from . import models
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields=['my_task']




class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]