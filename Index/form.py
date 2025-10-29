from django import forms
from .models import Myself

class MyselfForm(forms.ModelForm):
    class Meta:
        model = Myself
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your title'
            }),
            "description": forms.Textarea(attrs={
                'class': 'form-text',
                'placeholder': 'Enter your description',
                'rows': 4,
            }),
            "image": forms.ClearableFileInput(attrs={
                'class': 'form-input',
            }),
        }