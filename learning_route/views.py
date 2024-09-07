from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def detail(request, id: int):
    # id es el id de la ruta específica. por ahora no se usa.
    return render(request, 'detail.html')
