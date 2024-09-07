from django.shortcuts import render

def home(request):
    return render(request, 'learning_route.html')

def detail(request, id: int):
    # id es el id de la ruta específica. por ahora no se usa.
    return render(request, 'learning_route_detail.html')
