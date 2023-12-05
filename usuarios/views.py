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
from django.db.models import Count, Sum

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        if 'agua_form' in request.POST:
            form = AguaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                messages.success(request, 'Registro de agua guardado correctamente.')
                return redirect('home')
            else:
                messages.error(request, 'Ha ocurrido un error al guardar el registro de agua.')
        elif 'bloqueador_form' in request.POST:
            form = BloqueadorForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                messages.success(request, 'Registro de bloqueador guardado correctamente.')
                return redirect('home')
            else:
                messages.error(request, 'Ha ocurrido un error al guardar el registro de bloqueador.')
        elif 'ropa_form' in request.POST:
            form = RopaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                messages.success(request, 'Registro de ropa guardado correctamente.')
                return redirect('home')
            else:
                messages.error(request, 'Ha ocurrido un error al guardar el registro de ropa.')
    else:
        agua_form = AguaForm()
        bloqueador_form = BloqueadorForm()
        ropa_form = RopaForm()

    return render(request, 'registration/home.html', {
        'section': 'home',
        'agua_form': agua_form,
        'bloqueador_form': bloqueador_form,
        'ropa_form': ropa_form,
    })

def login_usuario(request):
    print("Entrando a la función login_usuario")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
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
            return redirect('home')
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
    if request.method == "POST":
        if 'agua_form' in request.POST:
            form = AguaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario =request.user
                registro.save()
                return redirect('home')
            
        elif 'bloqueador_form' in request.POST:
            form = BloqueadorForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                return redirect('home')
            
        elif 'ropa_form' in request.POST:
            form = RopaForm(request.POST)
            if form.is_valid():
                registro = form.save(commit=False)
                registro.usuario = request.user
                registro.save()
                return redirect('home')
    else:
        agua_form = AguaForm()
        bloqueador_form = BloqueadorForm()
        ropa_form = RopaForm()

    reportes_agua = RegistroAgua.objects.filter(usuario=request.user)
    reportes_bloqueador = RegistroBloqueador.objects.filter(usuario=request.user)
    reportes_ropa = RegistroRopa.objects.filter(usuario=request.user)

    total_vasos_agua = RegistroAgua.objects.filter(usuario=request.user, tipo_agua='V').count()
    total_botellas_agua = RegistroAgua.objects.filter(usuario=request.user, tipo_agua='B').count()
    total_bloqueador = RegistroBloqueador.objects.filter(usuario=request.user).count()
    total_ropa = RegistroRopa.objects.filter(usuario=request.user).count()

    reportes_agua_data = [{'tipo_agua': r.tipo_agua, 'fecha': r.fecha, 'cantidad_unidades': r.cantidad_unidades, 'nombre_usuario': r.usuario.username} for r in reportes_agua]
    reportes_bloqueador_data = [{'confirmacion_bloqueador': r.confirmacion_bloqueador, 'fecha': r.fecha, 'nombre_usuario': r.usuario.username} for r in reportes_bloqueador]
    reportes_ropa_data = [{'confirmacion_ropa': r.confirmacion_ropa, 'fecha': r.fecha, 'nombre_usuario': r.usuario.username} for r in reportes_ropa]

    print(f"Total de vasos de agua: {total_vasos_agua}")
    print(f"Total de botellas de agua: {total_botellas_agua}")
    print(f"Total de reportes de bloqueador: {total_bloqueador}")
    print(f"Total de reportes de ropa: {total_ropa}")
    return render(request, 'reporte.html', {
        'agua_form': agua_form,
        'bloqueador_form': bloqueador_form,
        'ropa_form': ropa_form,
        'reportes_agua': reportes_agua_data,
        'reportes_bloqueador': reportes_bloqueador_data,
        'reportes_ropa': reportes_ropa_data,
        'total_vasos_agua': total_vasos_agua,
        'total_botellas_agua': total_botellas_agua,
        'total_bloqueador': total_bloqueador,
        'total_ropa': total_ropa,
    })
        