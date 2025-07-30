from django.urls import path
from . import views

app_name = 'todo_task'

urlpatterns = [
    path('lists/', views.task_list, name = 'task-list'),
    path('details/<slug:slug_link>', views.task_detail, name = 'task-detail' ),
    path('new_task/', views.new_task, name = 'new-task'),
    path('update/<slug:slug_link>', views.update_task, name = 'update-task'),
    path('delete/<slug:slug_link>', views.delete_task, name = 'delete-task'),
]
