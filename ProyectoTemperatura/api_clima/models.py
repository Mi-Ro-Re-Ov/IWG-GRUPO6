# api_clima/models.py
from django.db import models

class InformacionClimatica(models.Model):
    ciudad = models.CharField(max_length=255)
    temperatura = models.FloatField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Información Climática - {self.ciudad}"