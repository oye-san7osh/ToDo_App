from django.shortcuts import render
from . models import Task


# Create your views here.

def task_list(request):
    return render(request, "todo_task/task_list.html")
