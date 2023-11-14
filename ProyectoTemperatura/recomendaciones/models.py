# recomendaciones/models.py
from django.db import models
from usuarios.models import PerfilUsuario

class Recomendacion(models.Model):
    perfil_usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255)
    contenido = models.TextField()

    def __str__(self):
        return f"Recomendación - {self.tipo} - {self.perfil_usuario.usuario.username}"