# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from .models import Task, Category
# from creator.models import Author  # Author model from your main app
# from .serializers import TaskSerializer


# # View to create a task and associate it with a category
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])  # Ensure user is authenticated
# def create_task(request):
#     try:
#         # Check if the user is authenticated
#         if request.user.is_anonymous:
#             return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

#         # Get the author associated with the logged-in user
#         author = Author.objects.get(user=request.user)

#         # Extract data from request
#         task_title = request.data.get('task_title')
#         task_details = request.data.get('task_details')
#         category_id = request.data.get('category_id')

#         # Ensure category exists
#         try:
#             category = Category.objects.get(pk=category_id)
#         except Category.DoesNotExist:
#             return Response({'error': 'Category does not exist'}, status=status.HTTP_400_BAD_REQUEST)

#         # Create the task and associate it with the author
#         task = Task.objects.create(task_title=task_title, task_details=task_details, category=category)

#         # Add the created task to the author's 'my_task' list
#         author.my_task.add(task)

#         return Response({'message': 'Task successfully created and added to your list'}, status=status.HTTP_201_CREATED)

#     except Author.DoesNotExist:
#         return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# # View to list tasks for the authenticated user
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Ensure user is authenticated
# def list_user_tasks(request):
#     try:
#         # Check if the user is authenticated
#         if request.user.is_anonymous:
#             return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

#         # Get the author associated with the logged-in user
#         author = Author.objects.get(user=request.user)

#         # Retrieve and serialize tasks
#         tasks = author.my_task.all()
#         serialized_tasks = TaskSerializer(tasks, many=True)

#         return Response(serialized_tasks.data, status=status.HTTP_200_OK)

#     except Author.DoesNotExist:
#         return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)





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