from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import UsuarioCustom
from registros.forms import AguaForm, RopaForm, BloqueadorForm
from registros.models import RegistroAgua, RegistroRopa, RegistroBloqueador
from django.db.models import Count
from registros.views import mostrar_contador
from .temp import obtener_temperatura
# from recomendaciones.views import combined_view as vista_recomendaciones
# from recomendaciones.models import recomendaciones

# Create your views here.
@login_required
def principal(request):

    # variable_vista_recomendaciones = vista_recomendaciones(request)

    if request.method == 'POST':
        if 'agua_form' in request.POST:
            form = AguaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                messages.success(request, 'Registro de agua guardado correctamente.')
                return redirect('principal')
            else:
                messages.error(request, 'Ha ocurrido un error al guardar el registro de agua.')
        elif 'bloqueador_form' in request.POST:
            form = BloqueadorForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                messages.success(request, 'Registro de bloqueador guardado correctamente.')
                return redirect('principal')
            else:
                messages.error(request, 'Ha ocurrido un error al guardar el registro de bloqueador.')
        elif 'ropa_form' in request.POST:
            form = RopaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                messages.success(request, 'Registro de ropa guardado correctamente.')
                return redirect('principal')
            else:
                messages.error(request, 'Ha ocurrido un error al guardar el registro de ropa.')
    else:
        agua_form = AguaForm()
        bloqueador_form = BloqueadorForm()
        ropa_form = RopaForm()

    temperatura = obtener_temperatura()

    return render(request, 'registration/principal.html', {
        'section': 'principal',
        'agua_form': agua_form,
        'bloqueador_form': bloqueador_form,
        'ropa_form': ropa_form,
        'temperatura': temperatura,
    })


def login_usuario(request):
    print("Entrando a la función login_usuario")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('principal')
        else:
            messages.error(request, "Uh... Ha ocurrido un error. Verifica tu usuario o contraseña.")
            return redirect('login.html')
    else:
        return render(request, 'registration/login.html', {})
    
def logout_usuario(request):
    logout(request)
    messages.success(request, "Has cerrado sesión exitosamente.")
    return redirect('login')
    
def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('principal')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def perfil(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user)
    return render(request, 'perfil.html', {'form': form})

@login_required
def reporte(request):
    total_vasos_agua, total_botellas_agua, total_bloqueador, total_ropa = mostrar_contador(request)
    print("Total Vasos Agua:", total_vasos_agua)
    print("Total Botellas Agua:", total_botellas_agua)
    print("Total Bloqueador:", total_bloqueador)
    print("Total Ropa:", total_ropa)

    test = "Variable de prueba"

    if request.method == "POST":
        if 'agua_form' in request.POST:
            form = AguaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario =request.user
                registro.save()
                return redirect('principal')
            
        elif 'bloqueador_form' in request.POST:
            form = BloqueadorForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                return redirect('principal')
            
        elif 'ropa_form' in request.POST:
            form = RopaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                return redirect('principal')
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

    print("Total Vasos de Agua:", total_vasos_agua)
    print("Total Botellas de Agua:", total_botellas_agua)
    print("Total Bloqueador:", total_bloqueador)
    print("Total Ropa:", total_ropa)

    context = {
        'agua_form': agua_form,
        'bloqueador_form': bloqueador_form,
        'ropa_form': ropa_form,
        'reportes_agua': reportes_agua_data,
        'reportes_bloqueador': reportes_bloqueador_data,
        'reportes_ropa': reportes_ropa_data,
        'vasos_totales': total_vasos_agua,
        'botellas_totales': total_botellas_agua,
        'total_bloqueador': total_bloqueador,
        'total_ropa': total_ropa,
    }

    print("Contexto:", context)
    return render(request, 'reporte.html', context)

