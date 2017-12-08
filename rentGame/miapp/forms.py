from django.contrib.auth.forms import UserCreationForm
from django import forms

class Usuario_form(UserCreationForm):
    telefono = forms.IntegerField()
    email = forms.CharField(max_length=30)
    address = forms.CharField(max_length=30)
