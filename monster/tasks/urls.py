from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('tasks', TaskList.as_view()),
    path('tasks/<str:task_id>', TaskDetail.as_view()),
]
