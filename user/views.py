from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def register(request):
    return render(request, 'register.html')