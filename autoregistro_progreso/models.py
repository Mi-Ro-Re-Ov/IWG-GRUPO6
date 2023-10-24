from django.db import models

# Create your models here.

class agua(models.Model):
    cant_agua = models.IntegerField()
    # Vaso = 250 mL
    # Botella = 500 mL

class ropa(models.Model):
    vestuario = models.BooleanField()

class bloqueador(models.Model):
    proteccion = models.BooleanField()

class fecha(models.Model):
    fecha_registro = models.CharField(max_length=50)

class hora(models.Model):
    hora_registro = models.CharField(max_length=50)

    