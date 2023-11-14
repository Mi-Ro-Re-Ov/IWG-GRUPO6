from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registro/', views.registro, name="registro"),
    path('olvidar_contrasena/', views.olvidar_contrasena, name="olvidar_contrasena"),
    path('perfil/', views.perfil, name="perfil"),
    path('mas_opciones/', views.mas_opciones, name='mas_opciones'),
]