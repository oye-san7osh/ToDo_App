from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Task


# Create your views here.
@login_required(login_url = "users:user-login")
def task_list(request):
    tasklists = Task.objects.all()
    return render(request, "todo_task/task_list.html",
                  {"tasklists": tasklists})
    
@login_required(login_url = "users:user-login")
def task_detail(request, slug_link):
    taskdetail = Task.objects.get(slug = slug_link)
    return render(request, "todo_task/task_details.html",
                  {"taskdetail": taskdetail})
