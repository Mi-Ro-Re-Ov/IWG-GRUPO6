from django import forms

from recomendaciones.models import cantidad_usuario

class CantidadForm(forms.ModelForm):
    class Meta:
        model = cantidad_usuario
        fields = [
            'usuario',
            'vasos_cont',
            'botellas_cont',
            'bloqueador_cont',
            'ropa_cont',
        ]