from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')

def detail(request, id: int):
    # id es el id del recurso específico. por ahora no se usa.
    return render(request, 'detail.html')
