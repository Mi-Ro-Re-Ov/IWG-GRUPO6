from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser
from django.db.models.signals import post_save

# Create your models here.
class UsuarioCustom(AbstractUser):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField(blank=False, default='')
    edad = models.PositiveIntegerField(null=True, blank=True, default=None)
    SEXO_CHOICES = [
        ("M", "Masculino"), ("F", "Femenino"), ("O", "Otro")
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default="O")
    peso = models.PositiveIntegerField(verbose_name="Peso (kg)", null=True, blank=True, default=None)
    altura = models.FloatField(verbose_name="Altura (m)", help_text="Utilice comas. Formato X,XX", null=True, blank=True, default=None)
    ciudad = models.CharField(max_length=20, null=True, blank=True, default=None)
    
    USERNAME_FIELD = 'username'
    REQUIERED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username