"""
URL configuration for ProyectoTemperatura2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.principal, name='principal')
Class-based views
    1. Add an import:  from other_app.views import principal
    2. Add a URL to urlpatterns:  path('', principal.as_view(), name='principal')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from recomendaciones.system import contar_usuario
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.principal, name="principal"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_usuario, name="logout"),
    path('registro/', views.registro, name="registro"),
    path('perfil/', views.perfil, name="perfil"),
    #path('anadir_cont/', contar_usuario, name="anadir_cont"),
]
