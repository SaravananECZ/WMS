# accounts/forms.py

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

from django import forms
from .models import UserProfile
from django.utils import timezone
from django.core.exceptions import ValidationError
import random

class RegistrationForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=True)
    otp = forms.CharField(max_length=6, required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

   