from django import forms
from .models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "skill_type", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "skill_type": forms.Select(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
