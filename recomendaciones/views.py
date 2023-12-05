from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import UsuarioCustom


@login_required
def combined_view(request):
    pass
    '''
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