from django.shortcuts import render

def home(request):
    return render(request, 'user.html')

def login(request):
    return render(request, 'user_login.html')

def logout(request):
    return render(request, 'user_logout.html')

def register(request):
    return render(request, 'user_register.html')