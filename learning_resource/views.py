from django.shortcuts import render

def home(request):
    return render(request, 'learning_resource.html')

def create(request):
    return render(request, 'learning_resource_create.html')

def detail(request, id: int):
    # id es el id del recurso específico. por ahora no se usa.
    return render(request, 'learning_resource_detail.html')
