from django.urls import path
from . import views

urlpatterns = [
    path('creators/', views.AuthorList.as_view())
]