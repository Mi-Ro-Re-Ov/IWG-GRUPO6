from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PerfilUsuario
from django.contrib.auth.models import User

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = '__all__'

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

