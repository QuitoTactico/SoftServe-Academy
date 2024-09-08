from django.shortcuts import render, redirect
from django import forms
from .models import LearningResource

class LearningResourceForm(forms.ModelForm):
    class Meta:
        model = LearningResource
        fields = ['name', 'mediaType', 'contentType', 'link', 'details', 'duration', 'language', 'originalPlatform', 'originalAuthor', 'generalLevel', 'learningSkills', 'requiredSkills']
        #fields = ['name', 'mediaType', 'contentType', 'link', 'details', 'duration', 'language', 'originalPlatform', 'originalAuthor', 'contentManager', 'generalLevel', 'learningSkills', 'requiredSkills', 'reviews']
        #widgets = {
        #    'name': forms.TextInput(attrs={'class': 'form-control'}),
        #    'mediaType': forms.Select(attrs={'class': 'form-control'}),
        #    'contentType': forms.Select(attrs={'class': 'form-control'}),
        #    'link': forms.TextInput(attrs={'class': 'form-control'}),
        #    'details': forms.Textarea(attrs={'class': 'form-control'}),
        #    'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        #    'language': forms.Select(attrs={'class': 'form-control'}),
        #    'originalPlatform': forms.TextInput(attrs={'class': 'form-control'}),
        #    'originalAuthor': forms.TextInput(attrs={'class': 'form-control'}),
        #    'contentManager': forms.Select(attrs={'class': 'form-control'}),
        #    'generalLevel': forms.NumberInput(attrs={'class': 'form-control'}),
        #    'learningSkills': forms.SelectMultiple(attrs={'class': 'form-control'}),
        #    'requiredSkills': forms.SelectMultiple(attrs={'class': 'form-control'}),
        #    'reviews': forms.SelectMultiple(attrs={'class': 'form-control'}),
        #}

def home(request):
    return render(request, 'learning_resource.html')

def create(request):
    if request.method == 'POST':
        form = LearningResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a una URL de éxito
    else:
        form = LearningResourceForm()
    return render(request, 'learning_resource_create.html', {'form': form})

def detail(request, id: int):
    # id es el id del recurso específico. por ahora no se usa.
    return render(request, 'learning_resource_detail.html')
