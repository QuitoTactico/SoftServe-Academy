from django import forms
from .models import LearningResource, Review

class LearningResourceForm(forms.ModelForm):
    class Meta:
        model = LearningResource
        fields = [
            "name",
            "media_type",
            "content_type",
            "link",
            "details",
            "duration",
            "language",
            "original_platform",
            "original_author",
            "general_level",
            "learning_skills",
            "required_skills",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "custom-input"}),
            "media_type": forms.Select(attrs={"class": "custom-select"}),
            "content_type": forms.Select(attrs={"class": "custom-select"}),
            "link": forms.TextInput(attrs={"class": "custom-input"}),
            "details": forms.Textarea(attrs={"class": "custom-textarea"}),
            "duration": forms.NumberInput(attrs={"class": "custom-input"}),
            "language": forms.Select(attrs={"class": "custom-select"}),
            "original_platform": forms.TextInput(attrs={"class": "custom-input"}),
            "original_author": forms.TextInput(attrs={"class": "custom-input"}),
            "general_level": forms.NumberInput(attrs={"class": "custom-input"}),
            "required_skills": forms.SelectMultiple(attrs={"class": "form-control", "id": "id_required_skills"}),
            "learning_skills": forms.SelectMultiple(attrs={"class": "form-control", "id": "id_learning_skills"}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["comment", "rate"]
        widgets = {
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control custom-textarea",
                    "placeholder": "Type Something...",
                    "required": True,
                }
            ),
            "rate": forms.NumberInput(
                attrs={"class": "form-control custom-input", "min": 1, "max": 5, "required": True}
            ),
        }
        labels = {
            "comment": "Comment Something",
            "rate": "Rating (1-5)",
        }
