from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RegistroAgua, RegistroRopa, RegistroBloqueador
from usuarios.models import PerfilUsuario
from django.contrib.auth.models import User

class RegistroAguaForm(forms.ModelForm):
    class Meta:
        model = RegistroAgua
        fields = ['cantidad_unidades', 'tipo_agua']
        widgets = {'usuario': forms.HiddenInput(), 'perfil_usuario': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            perfil_usuario = PerfilUsuario.objects.get(usuario=user)
            self.fields['perfil_usuario'].initial = perfil_usuario
            self.fields['perfil_usuario'].widget.attrs['readonly'] = True
            self.fields['usuario'].inital = user
            self.fields['usuario'].widget.attrs['readonly'] = True

class RegistroRopaForm(forms.ModelForm):
    class Meta:
        model = RegistroRopa
        fields = ['confirmacion_ropa']
        widgets = {'usuario': forms.HiddenInput(), 'perfil_usuario': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            perfil_usuario = PerfilUsuario.objects.get(usuario = user)
            self.fields['perfil_usuario'].initial = perfil_usuario
            self.fields['perfil_usuario'].widget.attrs['readonly'] = True
            self.fields['usuario'].initial = user
            self.fields['usuario'].widget.attrs['readonly'] = True  

    confirmacion_ropa = forms.CharField(label='¿Usó la ropa recomendada? (S/N)', required=False)

class RegistroBloqueadorForm(forms.ModelForm):
    class Meta:
        model = RegistroBloqueador
        fields = ['confirmacion_bloqueador']
        widgets = {'usuario': forms.HiddenInput(), 'perfil_usuario': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            perfil_usuario = PerfilUsuario.objects.get(usuario=user)
            self.fields['perfil_usuario'].initial = perfil_usuario
            self.fields['perfil_usuario'].widget.attrs['readonly'] = True
            self.fields['usuario'].initial = user
            self.fields['usuario'].widget.attrs['readonly'] = True
            
    confirmacion_bloqueador = forms.CharField(label='¿Ha usado bloqueador? (S/N)', required=False)