from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task, Category
from creator.models import Author  # Author model from your main app
from .serializers import TaskSerializer


# View to create a task and associate it with a category
@api_view(['POST'])
def create_task(request):
    try:
        author = Author.objects.get(user=request.user)
        task_title = request.data.get('task_title')
        task_details = request.data.get('task_details')
        category_id = request.data.get('category_id')

        category = Category.objects.get(pk=category_id)
        task = Task.objects.create(task_title=task_title, task_details=task_details, category=category)

        # Add the created task to the author's 'my_task' list
        author.my_task.add(task)

        return Response({'message': 'Task successfully created and added to your list'}, status=status.HTTP_201_CREATED)

    except Category.DoesNotExist:
        return Response({'error': 'Category does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# View to list tasks for the authenticated user
@api_view(['GET'])
def list_user_tasks(request):
    try:
        author = Author.objects.get(user=request.user)
        tasks = author.my_task.all()
        serialized_tasks = TaskSerializer(tasks, many=True)

        return Response(serialized_tasks.data, status=status.HTTP_200_OK)

    except Author.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)