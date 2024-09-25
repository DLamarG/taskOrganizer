from django.db import models

# Create your models here.


TITLE_CHOICES = (
    ("A", "Applications"),
    ("N", "Networking"),
    ("I", "Interviews"),
    ("C", "Coding"),
    ("P", "Projects"),
    ("D", "Development"),
)



class Category(models.Model):
    category_title = models.CharField(max_length=1, choices=TITLE_CHOICES)
    category_id = models.AutoField(primary_key=True)
