from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    edad_usuario = models.IntegerField()
    ciudad_usuario = models.CharField(max_length=50)
    comuna_usuario = models.CharField(max_length=50)
    insignias_totales = models.IntegerField()
    insignias_ganadas = models.IntegerField()