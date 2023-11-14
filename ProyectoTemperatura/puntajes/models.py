# puntajes/models.py
from django.db import models
from usuarios.models import PerfilUsuario

class Puntuacion(models.Model):
    perfil_usuario = models.OneToOneField(PerfilUsuario, on_delete=models.CASCADE)
    porcentaje = models.IntegerField(default=0)

class Meta(models.Model):
    perfil_usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    cantidad_objetivo = models.FloatField()

class Insignia(models.Model):
    nombre = models.CharField(max_length=255)
    # Otros campos según sea necesario.