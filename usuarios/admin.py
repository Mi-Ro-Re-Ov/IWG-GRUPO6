from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioCustom
from recomendaciones.models import recomendaciones
# Register your models here.

admin.site.register(recomendaciones)


