from django.db import models

# Create your models here.
class datos_api(models.Model):
    dato_api_temperatura = models.IntegerField()
    dato_api_radiacion = models.IntegerField()

class recomendaciones(models.Model):
    reco_mañana = models.CharField(max_length=100)
    reco_tarde = models.CharField(max_length=100)
    reco_noche = models.CharField(max_length=100)

# class tiempo_registro(models.Model):
    # tiempo_registro