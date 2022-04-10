from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    return render (request,'App/inicio.html')
   

def jugadoresFormulario(request):

    if request.method == "POST":
        myForm = JugadoresFormulario(request.POST)                                                                                    #llega info del html

        print(myForm)
        
        if myForm.is_valid:

            information = myForm.cleaned_data
            nuevoJugador = jugadores(nombre=information['nombre'], edad=information['edad'], nivel=information['nivel']) 
            nuevoJugador.save()                                                                                                 #Guardamos datos
            return render(request, 'App/inicio.html')                                                                        #volvemos al inicio de la pagina de jugadores con datos limpios
    else:
        myForm = JugadoresFormulario()     
                                                                                               #si no hay POST, me devuelvo el html normal
    return render (request, 'App/jugadores.html', {"myForm":myForm})



def entrenadores(request):
    return render (request, 'App/entrenadores.html')



def sponsors(request):
    return render (request, 'App/sponsors.html')