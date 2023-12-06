from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import cantidad_usuario, recomendaciones, proxy
from usuarios.models import UsuarioCustom
from recomendaciones.forms import CantidadForm

@login_required
def combined_view(request):
    current_user = request.user

    user_recommendations = recomendaciones.objects.filter()

    if not user_recommendations.exists():
        return render(request, 'combined_view.html', {'error_message': 'No hay recomendaciones pendientes.'})

    recomendacion_azar = user_recommendations.order_by('?').first()

    recomendacion_azar.completado = True
    recomendacion_azar.save()

    contexto = {'recomendacion': recomendacion_azar}
    return render(request, 'combined_view.html', contexto)

'''
@login_required
def combined_view(request):
    current_user = request.user

    if request.method == 'GET':
        try:
            user_recommendations = recomendaciones.objects.filter(usuario=current_user)
            user_proxy_values = proxy.objects.get()

            recomendacion_azar = recomendaciones.objects.order_by('?').first()
            if user_recommendations.exists():
                mapping_dictionary = {
                    'vasos': 10, 
                    'botellas': 10,
                    'bloqueador': 10,
                    'ropa': 10,
                }

                if mapping_dictionary.get(recomendacion_azar.palabra_clave, 0) >= recomendacion_azar.numero:
                    recomendacion_azar.completado = True
                else:
                    recomendacion_azar.completado = False

                recomendacion_azar.usuario = current_user
                recomendacion_azar.save()

                contexto = {'recomendacion': recomendacion_azar}
                return render(request, 'combined_view.html', contexto)

        except recomendaciones.DoesNotExist:
            return render(request, 'combined_view.html', {'error_message': 'No recommendation found for the user.'})

        except proxy.DoesNotExist:
            return render(request, 'combined_view.html', {'error_message': 'No proxy values found in the database.'})

    else:
        return HttpResponse('Unsupported HTTP method')
    '''
    
    

def contar_usuario(request):
    cantidades = cantidad_usuario.objects.filter(usuario=request.user)

    if request.method == "POST":
        form = CantidadForm(request.POST)
        
        if form.is_valid():
            form.save()
            form = CantidadForm()
            return render(request, 'formulario.html', {'form': form})
        
    return HttpResponse('Unsupported HTTP method or invalid form submission')




def contar_usuario(request):
   cantidades = cantidad_usuario.objects.filter(usuario=request.user)
   if request.method == "POST":
      form = CantidadForm(request.POST)

      if form.is_valid():
        form.save()
        form= CantidadForm()
        return render(request, "lformulario.html", {'form': form})
      