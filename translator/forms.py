from django import forms
from .models import BinaryTranslation

class BinaryTranslationForm(forms.ModelForm):
    binary_code = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter binary code here...'}))

    class Meta:
        model = BinaryTranslation
        fields = ['binary_code']
