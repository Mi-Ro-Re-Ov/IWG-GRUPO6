from django.http import HttpResponse

def prueba(request):
    return HttpResponse("<h1>Hola Mundo</h1>")