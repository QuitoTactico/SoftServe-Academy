from django.shortcuts import render, redirect
from django import forms
from .models import Preference

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ['mediaType', 'contentType', 'learningType', 'timePerWeek', 'timePerSession']
        #widgets = {
        #    'mediaType': forms.Select(attrs={'class': 'form-control'}),
        #    'contentType': forms.Select(attrs={'class': 'form-control'}),
        #    'learningType': forms.Select(attrs={'class': 'form-control'}),
        #    'timePerWeek': forms.NumberInput(attrs={'class': 'form-control'}),
        #    'timePerSession': forms.NumberInput(attrs={'class': 'form-control'}),
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
