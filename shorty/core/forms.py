from django import forms
from .models import shorties


class shorties_form(forms.ModelForm):
    class Meta:
        model = shorties
        fields = ["original"]
