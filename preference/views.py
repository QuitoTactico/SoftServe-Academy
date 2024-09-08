from django.shortcuts import render, redirect
from .models import Preference
from .forms import PreferenceForm

def create(request):
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')  # Redirige a una URL de éxito
    else:
        form = PreferenceForm()
    return render(request, 'preference_create.html', {'form': form})

def detail(request, id: int):
    #id es el id del usuario. por ahora no se usa.
    return render(request, 'preference_detail.html')
