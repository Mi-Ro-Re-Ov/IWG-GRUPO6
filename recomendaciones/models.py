from django.db import models

# Create your models here.
class dato_temperatura(models.Model):
    dato_api_temperatura = models.IntegerField()

class dato_radiacion(models.Model):
    dato_api_radiacion = models.IntegerField()

# class tiempo_registro(models.Model):
    # tiempo_registro

class recomendacion_mañana(models.Model):
    reco_mañana = models.CharField(max_length=100)

class recomendacion_tarde(models.Model):
    reco_tarde = models.CharField(max_length=100)

class recomendacion_noche(models.Model):
    reco_noche = models.CharField(max_length=100)

    