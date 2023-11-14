# datos_curiosos/models.py
from django.db import models

class DatoCurioso(models.Model):
    contenido = models.TextField()

    def __str__(self):
        return f"Dato Curioso - {self.id}"