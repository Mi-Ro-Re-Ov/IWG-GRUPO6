from django.contrib import admin
from .models import PerfilUsuario
# Register your models here.
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "correo", "edad", "sexo", "peso", "altura"]


admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
