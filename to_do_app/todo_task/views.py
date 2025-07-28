from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Task
from . import forms


# Create your views here.

def task_list(request):
    if request.user.is_superuser:
        tasklists = Task.objects.all().order_by('-event_date')
    else:
        tasklists = Task.objects.filter(created_by = request.user).order_by('-event_date')
    return render(request, "todo_task/task_list.html",
                  {"tasklists": tasklists})
    

def task_detail(request, slug_link):
    taskdetail = Task.objects.get(slug_link = slug_link)
    return render(request, "todo_task/task_details.html",
                  {"taskdetail": taskdetail})
    
   
def new_task(request):
    if request.method == "POST":
        form = forms.CreateTask(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit = False)
            task.created_by = request.user
            task.save()
            return redirect("todo_task:task-list")
    else:
        form = forms.CreateTask()
    return render(request, "todo_task/task_new.html", {"form": form} )
