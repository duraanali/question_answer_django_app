from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Questions, Person, Answers

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['user']
        
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
        fields = ["title", "description"]
        

class editQuestion(forms.ModelForm):

    class Meta:
        model = Questions
        fields = ["title", "description", "status"]
        
        
class AnswerQuestion(forms.ModelForm):

    class Meta:
        model = Answers
        fields = ["reply"]
        widgets = {
            'question_id': forms.HiddenInput(),
            'user': forms.HiddenInput()

        }
