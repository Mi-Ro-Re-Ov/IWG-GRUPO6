from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseServerError
from django.urls import reverse
from usuarios.models import UsuarioCustom
from .forms import AguaForm, RopaForm, BloqueadorForm
from .models import RegistroAgua, RegistroBloqueador, RegistroRopa

# Create your views here.
def reporte(request):
    if request.method == "POST":
        if 'agua_form' in request.POST:
            form = AguaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                return redirect('reporte')
            
        elif 'bloqueador_form' in request.POST:
            form = BloqueadorForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                return redirect('reporte')
            
        elif 'ropa_form' in request.POST:
            form = RopaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                return redirect('reporte')
            
    else:
        agua_form = AguaForm()
        bloqueador_form = BloqueadorForm()
        ropa_form = RopaForm()

    reportes_agua = RegistroAgua.objects.filter(usuario=request.user)
    reportes_bloqueador = RegistroBloqueador.objects.filter(usuario=request.user)
    reportes_ropa = RegistroRopa.objects.filter(usuario=request.user)

    reportes_agua_data = [{'tipo_agua': r.tipo_agua, 'fecha': r.fecha, 'cantidad_unidades': r.cantidad_unidades, 'nombre_usuario': r.usuario.username} for r in reportes_agua]
    reportes_bloqueador_data = [{'confirmacion_bloqueador': r.confirmacion_bloqueador, 'fecha': r.fecha, 'nombre_usuario': r.usuario.username} for r in reportes_bloqueador]
    reportes_ropa_data = [{'confirmacion_ropa': r.confirmacion_ropa, 'fecha': r.fecha, 'nombre_usuario': r.usuario.username} for r in reportes_ropa]

    print(reportes_agua)
    return render(request, 'reporte.html', {
        'agua_form': agua_form,
        'bloqueador_form': bloqueador_form,
        'ropa_form': ropa_form,
        'reportes_agua': reportes_agua_data,
        'reportes_bloqueador': reportes_bloqueador_data,
        'reportes_ropa': reportes_ropa_data,
    })

def mostrar_contador(request):
    usuario = request.user

    registros_agua_usuario = RegistroAgua.objects.filter(usuario=usuario)
    
    total_vasos = 0
    total_botellas = 0

    for registro_agua in registros_agua_usuario:
        if registro_agua.tipo_agua == "V":
            total_vasos += registro_agua.cantidad_unidades
        elif registro_agua.tipo_agua == "B":
            total_botellas += registro_agua.cantidad_unidades

    total_bloqueador = RegistroBloqueador.objects.filter(usuario=usuario).count()
    total_ropa = RegistroRopa.objects.filter(usuario=usuario).count()

    return total_vasos, total_botellas, total_bloqueador, total_ropa