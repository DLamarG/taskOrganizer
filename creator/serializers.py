from rest_framework import serializers
from . import models
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields=['my_task']



class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        # Hash the password before saving
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
# class SignupSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "password"]