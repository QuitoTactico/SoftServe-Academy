from django import forms
from .models import User
from skill.models import SkillLevel


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["name", "email", "password"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("The passwords do not match")


class CurrentSkillsForm(forms.ModelForm):
    current_skills = forms.ModelMultipleChoiceField(
        queryset=SkillLevel.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        required=False,
        label="Current Skills",
    )

    class Meta:
        model = User
        fields = ["current_skills"]


class TargetSkillsForm(forms.ModelForm):
    target_skills = forms.ModelMultipleChoiceField(
        queryset=SkillLevel.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-control"}),
        required=False,
        label="Target Skills",
    )

    class Meta:
        model = User
        fields = ["target_skills"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "image"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your name"}
            ),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }
