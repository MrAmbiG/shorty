from django import forms
from .models import shorties


class shorties_form(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.label_suffix = ""  # Removes : as label suff
    #     self.fields['original'].label = '' # removes label
    class Meta:
        model = shorties
        fields = ["original"]
        # widgets = {
        #     'original': forms.TextInput(attrs={'placeholder': 'Enter URL'}),
        # }

    # def clean(self):
    #     cleaned_data = super(ContactForm, self).clean()
    #     original = cleaned_data.get('original')
    #     if not original:
    #         raise forms.ValidationError('Input a URL')
