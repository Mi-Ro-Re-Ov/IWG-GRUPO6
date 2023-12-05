from django.db import models
from django.conf import settings

# Create your models here.

class RegistroAgua(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad_unidades = models.PositiveIntegerField(default=1)
    AGUA_CHOICES = [
        ('V', 'Vasos'),
        ('B', 'Botellas'),
    ]
    tipo_agua = models.CharField(max_length=1, choices=AGUA_CHOICES)

    def __str__(self):
        return f"{self.usuario.username} - {self.tipo_agua} - {self.fecha}"

class RegistroBloqueador(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    BLOQUEADOR_CHOICES = [('S', 'Sí'), ('N', 'No')]
    confirmacion_bloqueador = models.CharField(max_length=1, choices=BLOQUEADOR_CHOICES)

    def __str__(self):
        return f"{self.usuario.username} - {self.confirmacion_bloqueador} - {self.fecha}"
    
class RegistroRopa(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    ROPA_CHOICES = [('S', 'Sí'), ('N', 'No')]
    confirmacion_ropa = models.CharField(max_length=1, choices=ROPA_CHOICES)

    def __str__(self):
        return f"{self.usuario.username} - {self.confirmacion_ropa} - {self.fecha}"
    