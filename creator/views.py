from rest_framework import generics
from . import serializers
from . import models
# Create your views here.

class AuthorList(generics.ListAPIView):
    queryset = models.Author.objects.all()
    serializer_class=serializers.AuthorSerializer
