from django import forms
from .models import LearningResource

class LearningResourceForm(forms.ModelForm):
    class Meta:
        model = LearningResource
        fields = ['name', 'media_type', 'content_type', 'link', 'details', 'duration', 'language', 'original_platform', 'original_author', 'general_level', 'learning_skills', 'required_skills']
        #fields = ['name', 'media_type', 'content_type', 'link', 'details', 'duration', 'language', 'original_platform', 'original_author', 'content_manager', 'general_level', 'learning_skills', 'required_skills', 'reviews']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'media_type': forms.Select(attrs={'class': 'form-control'}),
            'content_type': forms.Select(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'original_platform': forms.TextInput(attrs={'class': 'form-control'}),
            'original_author': forms.TextInput(attrs={'class': 'form-control'}),
        #   'content_manager': forms.Select(attrs={'class': 'form-control'}),
            'general_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'learning_skills': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'required_skills': forms.SelectMultiple(attrs={'class': 'form-control'}),
        #   'reviews': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }