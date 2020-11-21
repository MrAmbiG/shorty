from django import forms
from .models import *


class shorties_form(forms.ModelForm):
    class Meta:
        model = shorties
        fields = ["original", "alias"]
