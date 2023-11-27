from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('registro/', views.registro, name="registro"),
    path('olvidar_contrasena/', views.olvidar_contrasena, name="olvidar_contrasena"),
    path('perfil/', views.perfil, name="perfil"),
    path('mas_opciones/', views.mas_opciones, name='mas_opciones'),
    path('test/', views.test, name="test")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    