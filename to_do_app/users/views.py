from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomUserRegisterForm
from django.contrib import messages

# Create your views here.

def user_register(request):
    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("users:user-login")
    else:
        form = CustomUserRegisterForm()
    return render(request, "users/register.html", {"form" : form})
            

def user_login(request):
    return render(request, "users/login.html")

def user_logout(request):
    return render(request, "users/logout.html")