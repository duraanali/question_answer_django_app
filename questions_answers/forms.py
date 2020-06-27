from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Questions

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    country = forms.CharField()
    bio = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "country", "bio", "password1", "password2"]
        

class askQuestion(forms.ModelForm):
   
    
    class Meta:
        model = Questions
        fields = ["title", "description", "status"]
