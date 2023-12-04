from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioCustom

class RegistroForm(UserCreationForm):
    class Meta:
        model = UsuarioCustom
        fields = ('username', 'email', 'password1', 'password2',)


class PerfilForm(forms.ModelForm):
    class Meta:
        model = UsuarioCustom
        fields = ('username', 'email', 'nombre', 'apellido', 'edad', 'sexo', 'peso', 'altura', 'ciudad')