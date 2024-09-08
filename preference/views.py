from django.shortcuts import render, redirect
from django import forms
from .models import Preference

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ['media_type', 'content_type', 'learning_type', 'time_per_week', 'time_per_session']
        #widgets = {
        #    'media_type': forms.Select(attrs={'class': 'form-control'}),
        #    'content_type': forms.Select(attrs={'class': 'form-control'}),
        #    'learning_type': forms.Select(attrs={'class': 'form-control'}),
        #    'time_per_week': forms.NumberInput(attrs={'class': 'form-control'}),
        #    'time_per_session': forms.NumberInput(attrs={'class': 'form-control'}),
        #}

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
