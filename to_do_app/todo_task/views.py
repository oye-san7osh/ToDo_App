from django.shortcuts import render
from . models import Task


# Create your views here.

def task_list(request):
    tasklists = Task.objects.all()
    return render(request, "todo_task/task_list.html",
                  {"tasklists": tasklists})
    
    
def task_detail(request):
    taskdetail = Task.objects.get(slug = slug_link)
    return render(request, "todo_task/task_details.html",
                  {"taskdetail": taskdetail})
