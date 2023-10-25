from django.db import models

# Create your models here.

class registro(models.Model):
    cant_agua = models.IntegerField()
    # Vaso = 250 mL
    # Botella = 500 mL
    vestuario = models.BooleanField()
    bloqueador = models.BooleanField()
    fecha_registro = models.CharField(max_length=50)
    hora_registro = models.CharField(max_length=50)
