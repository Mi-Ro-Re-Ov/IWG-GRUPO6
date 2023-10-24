from django.db import models

# Create your models here.
class insignias_ganadas(models.Model):
    insignias_ganadas_usuario = models.IntegerField()

class insignias_totales(models.Model):
    cant_insignias_totales = models.IntegerField()

class agua_tomada(models.Model):
    cant_agua_tomada = models.IntegerField

class bloqueador_aplicado(models.Model):
    # Cantidad de veces en las que el valor de Bloqueadro fue verdadero.
    cant_bloqueador_aplicado = models.IntegerField()

class ropa(models.Model):
    # Cantidad de veces en las que el valor de Ropa fue verdadero.
    cant_ropa_puesta = models.IntegerField()

# class tiempo(models.Model):
    # Debe definirse un modelo que incluya el tiempo, y permita realizar las operaciones lógicas del logro de las insignias.