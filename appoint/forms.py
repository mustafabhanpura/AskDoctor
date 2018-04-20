from django import forms
from .models import SignUp, Patient
from django.contrib.auth.models import User

class Sign(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','password',)
        help_texts={'username': None, 'password': None}

class Profile(forms.ModelForm):
    class Meta:
        model=SignUp
        exclude=['user']

class Query(forms.ModelForm):
    class Meta:
        model=Patient 
        exclude = ['medicine','answer']
