from django.urls import path
from . import views

app_name = 'todo_task'

urlpatterns = [
    path('lists/', views.task_list, name = 'task-list')
    
]
