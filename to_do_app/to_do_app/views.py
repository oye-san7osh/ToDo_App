from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'homepage.html')

@login_required(login_url = "users:user-login")
def about(request):
    return render(request, 'aboutpage.html')
