from django import forms
from .models import RegistroRopa, RegistroAgua, RegistroBloqueador

class AguaForm(forms.ModelForm):
    class Meta:
        model = RegistroAgua
        fields = ['cantidad_unidades', 'tipo_agua']

class BloqueadorForm(forms.ModelForm):
    class Meta:
        model = RegistroBloqueador
        fields = ['confirmacion_bloqueador']

class RopaForm(forms.ModelForm):
    class Meta:
        model = RegistroRopa
        fields = ['confirmacion_ropa']