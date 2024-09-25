from django.urls import path
from . import views

urlpatterns = [
    path('create-task/', views.create_task, name='create-task'),
    path('my-tasks/', views.list_user_tasks, name='list-user-tasks'),
]