from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from creator.views import SignupView




urlpatterns = [
    path('create-task/', views.create_task, name='create-task'),
    path('my-tasks/', views.list_user_tasks, name='list-user-tasks'),
    path('get-token/', obtain_auth_token),
    path('signup/', SignupView.as_view())
]