from rest_framework import serializers
from . import models




class CategorySerialzer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields=['category_title', 'category_id']