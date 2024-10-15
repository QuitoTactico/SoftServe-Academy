from django import forms
from django.core.exceptions import ValidationError
from .models import Preference


class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference  # Asegúrate de que esto corresponda a tu modelo
        fields = [
            "media_type",
            "content_type",
            "learning_type",
            "time_per_week",
            "time_per_session",
        ]

    def clean_time_per_week(self):
        time_per_week = self.cleaned_data.get("time_per_week")
        if time_per_week > 6000:
            raise ValidationError("Time per Week cannot be more than 6000 minutes.")
        return time_per_week

    def clean_time_per_session(self):
        time_per_session = self.cleaned_data.get("time_per_session")
        if time_per_session > 600:
            raise ValidationError("Time per Session cannot be more than 600 minutes.")
        return time_per_session
