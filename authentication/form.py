from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields =["username","first_name","last_name","email","password1","password2"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your email"}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['phone_number', 'profile_picture']
        widgets = {
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter phone number'}),
        }