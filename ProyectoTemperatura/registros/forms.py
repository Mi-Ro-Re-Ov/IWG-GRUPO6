from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RegistroAgua, RegistroRopa, RegistroBloqueador
from django.contrib.auth.models import User

class RegistroAguaForm(forms.ModelForm):
    class Meta:
        model = RegistroAgua
        fields = ['cantidad_unidades', 'tipo_agua']
        widgets = {'usuario': forms.HiddenInput()}

class RegistroRopaForm(forms.ModelForm):
    class Meta:
        model = RegistroRopa
        fields = ['confirmacion_ropa']
        widgets = {'usuario': forms.HiddenInput()}
        

    confirmacion_ropa = forms.CharField(label='¿Usó la ropa recomendada? (S/N)', required=False)

class RegistroBloqueadorForm(forms.ModelForm):
    class Meta:
        model = RegistroBloqueador
        fields = ['confirmacion_bloqueador']
        widgets = {'usuario': forms.HiddenInput()}

    confirmacion_bloqueador = forms.CharField(label='¿Ha usado bloqueador? (S/N)', required=False)