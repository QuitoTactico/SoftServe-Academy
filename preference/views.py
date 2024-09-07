from django.shortcuts import render

def create(request): 
    return render(request, 'preference_create.html')

def detail(request, id: int):
    #id es el id del usuario. por ahora no se usa.
    return render(request, 'preference_detail.html')
