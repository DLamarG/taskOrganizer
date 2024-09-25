from django.db import models
from django.contrib.auth.models import User
from task.models import Task




#Author model.
class Author(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    my_task = models.ManyToManyField(Task, related_name='my_task', blank=True)

    # class Meta:
    #     db_table = 'mylist_to_do'


    def add_to_task(self, task_title, task_details, task_id):
        if not self.my_task.filter(task_title=task_title).exists():
            task=Task.objects.create(task_id=task_id, task_title=task_title, task_details=task_details)
            self.my_task.add(task)
            return {'message': 'task added to your list of tasks'}
        else:
            return {'message': 'task already exist'}
        

    def __str__(self):
        return self.user.username

