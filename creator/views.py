from rest_framework import generics
from . import serializers
from . import models
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import SignupSerializer
from rest_framework.permissions import AllowAny
from .models import Author

class AuthorList(generics.ListAPIView):
    queryset = models.Author.objects.all()
    serializer_class=serializers.AuthorSerializer




# handles request and parses body for username and password
class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            #create_user is special method. must be used to create user
            user = User.objects.create_user(username=username, password=password)
            user_profile = Author(user=user)
            user_profile.save()