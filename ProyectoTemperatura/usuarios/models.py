from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PerfilUsuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(blank=False, default='')
    SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')]
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='O')
    peso = models.FloatField()
    altura = models.FloatField()

    def __str__(self):
        return self.usuario.username