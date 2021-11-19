from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *





class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ClienteForm(ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['user']
