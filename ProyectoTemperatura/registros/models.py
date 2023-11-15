# registros/models.py
from django.db import models
from django.contrib.auth.models import User
from usuarios.models import PerfilUsuario

class RegistroAgua(models.Model):
    TIPO_CHOICES = [
        ('V', 'Vasos'),
        ('B', 'Botellas'),
    ]
    perfil_usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad_unidades = models.IntegerField()
    tipo_agua = models.CharField(max_length=1, choices=TIPO_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.usuario:
            self.usuario = self.perfil_usuario.usuario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Registro de Agua - {self.perfil_usuario.usuario.username} - {self.fecha}"

    def cantidad_ml(self):
        if self.tipo_agua == 'V':
            return self.cantidad_unidades * 250
        elif self.tipo_agua == 'B':
            return self.cantidad_unidades * 500
        else:
            return 0

class RegistroBloqueador(models.Model):
    SI = "S"
    NO = "N"

    OPCIONES_CONFIRMACION_BLOQUEADOR = [(SI, 'Sí'), (NO, 'No')]

    perfil_usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    confirmacion_bloqueador = models.CharField(max_length=1, choices=OPCIONES_CONFIRMACION_BLOQUEADOR, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.usuario:
            self.usuario = self.perfil_usuario.usuario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Registro de Bloqueador - {self.perfil_usuario.usuario.username} - {self.fecha}"

class RegistroRopa(models.Model):
    SI = 'S'
    NO = 'N'
    OPCIONES_CONFIRMACION_ROPA = [(SI, 'Sí'), (NO, 'No')]

    perfil_usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    confirmacion_ropa = models.CharField(max_length=1, choices=OPCIONES_CONFIRMACION_ROPA)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.usuario:
            self.usuario = self.perfil_usuario.usuario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Registro de Ropa - {self.perfil_usuario.usuario.username} - {self.fecha}"