from django.contrib import admin
from . import models
from category.models import Category

# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Task)
admin.site.register(Category)