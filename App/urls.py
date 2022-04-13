from django.urls import path
from App import views


urlpatterns = [
    path('',views.inicio, name=""),
    path('jugadores',views.jugadoresFormulario, name="Jugadores"),
    path('entrendores',views.entrenadoresFormulario, name="Entrenadores"),
    path('sponsors',views.sponsorsFormulario, name="Sponsors"),
    path('buscar',views.buscar,name="buscar"),
    path('resultadoBusqueda',views.busqueda,name="busqueda"),
]