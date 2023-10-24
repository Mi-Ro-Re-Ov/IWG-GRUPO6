from django.db import models

# Create your models here.
class nombre(models.Model):
    nombre_usuario = models.CharField(max_length=100)

class edad(models.Model):
    edad_usuario = models.IntegerField()

class ciudad(models.Model):
    ciudad_usuario = models.CharField(max_length=50)

class comuna(models.Model):
    comuna_usuario = models.CharField(max_length=50)

class insignias_totales(models.Model):
    total = models.IntegerField()
    
class insignias_ganadas(models.Model):
    ganadas = models.IntegerField()