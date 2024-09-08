from django import forms
from .models import Preference

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ['media_type', 'content_type', 'learning_type', 'time_per_week', 'time_per_session']
        widgets = {
            'media_type': forms.Select(attrs={'class': 'form-control'}),
            'content_type': forms.Select(attrs={'class': 'form-control'}),
            'learning_type': forms.Select(attrs={'class': 'form-control'}),
            'time_per_week': forms.NumberInput(attrs={'class': 'form-control'}),
            'time_per_session': forms.NumberInput(attrs={'class': 'form-control'}),
        }