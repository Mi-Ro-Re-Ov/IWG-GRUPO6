from django.urls import include, path
from .views import combined_view

urlpatterns = [
        path('random/', combined_view, name = 'update completado'),
        
]
