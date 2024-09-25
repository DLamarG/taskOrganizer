from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=50, blank=False)
    task_details = models.CharField(max_length=1000, blank=False)
    # task_details = models.CharField(max_length=1000, blank=False)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title

