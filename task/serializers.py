from rest_framework import serializers
from . import models


class TaskSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model=models.Task
        fields = ['task_id', 'task_title', 'task_details', 'category']