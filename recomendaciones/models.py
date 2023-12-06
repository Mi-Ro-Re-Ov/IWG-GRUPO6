from django.db import models
from django.contrib.auth.models import User
from usuarios.models import UsuarioCustom

# Create your models here.
class datos_api(models.Model):
    dato_api_temperatura = models.IntegerField()
    dato_api_radiacion = models.IntegerField()

class recomendaciones(models.Model):
    info = models.TextField(blank=True)
    numero = models.IntegerField(null=True)
    palabra_clave = models.TextField(default='vasos')
    completado = models.BooleanField(null=True)
    usuario = models.ForeignKey(UsuarioCustom, on_delete=models.CASCADE)

    def __str__(self):
        return f"Recomendación para {self.usuario.username} - {self.palabra_clave} - {self.numero}"

class proxy(models.Model):
    vasos = models.IntegerField(default=10)
    botellas = models.IntegerField(default=10)
    bloqueador = models.IntegerField(default=10)
    ropa = models.IntegerField(default=10)

class cantidad_usuario(models.Model):
    usuario = models.ForeignKey(UsuarioCustom, on_delete=models.CASCADE)
    vasos_cont = models.PositiveIntegerField()
    botellas_cont = models.PositiveIntegerField()
    bloqueador_cont = models.PositiveIntegerField()
    ropa_cont = models.PositiveIntegerField()

    def __str__(self):
        return f"Cantidad para {self.usuario.username} - Vasos: {self.vasos_cont}, Botellas: {self.botellas_cont}, Bloqueador: {self.bloqueador_cont}, Ropa: {self.ropa_cont}"
