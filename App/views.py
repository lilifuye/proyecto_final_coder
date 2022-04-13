from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
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
            nuevoJugador.save()                                                                                         #Guardamos datos
            return render(request, 'App/inicio.html')                                                                        #volvemos al inicio de la pagina de jugadores con datos limpios
    else:
        myForm = JugadoresFormulario()     
                                                                                                                            #si no hay POST, me devuelvo el html normal
    return render (request, 'App/jugadores.html', {"myFormJugadores":myForm})




def entrenadoresFormulario(request):

    if request.method == "POST":
        myForm = EntrenadoresFormulario(request.POST)                                                                                    #llega info del html

        print(myForm)
        
        if myForm.is_valid:
            information = myForm.cleaned_data
            nuevoEntrenador = entrenadores(nombre=information['nombre'], edad=information['edad'], equipo=information['equipo']) 
            nuevoEntrenador.save()                                                                                #Guardamos datos
            return render(request, 'App/inicio.html')                                                                        #volvemos al inicio de la pagina de jugadores con datos limpios
    else:
        myForm = EntrenadoresFormulario()     
                                                                                                                            #si no hay POST, me devuelvo el html normal
    return render (request, 'App/entrenadores.html', {"myFormEntrenadores":myForm})




def sponsorsFormulario(request):

    if request.method == "POST":
        myForm = SponsorsFormulario(request.POST)                                                                                    #llega info del html

        print(myForm)
        
        if myForm.is_valid:

            information = myForm.cleaned_data
            nuevoSponsor = sponsors(nombre=information['nombre'], edad=information['edad'], producto=information['producto']) 
            nuevoSponsor.save()                                                                                         #Guardamos datos
            return render(request, 'App/inicio.html')                                                                        #volvemos al inicio de la pagina de jugadores con datos limpios
    else:
        myForm = SponsorsFormulario()     
                                                                                                                            #si no hay POST, me devuelvo el html normal
    return render (request, 'App/sponsors.html', {"myFormSponsors":myForm})




def busqueda(request):
    respuesta = f"Búsqueda: {request.GET['jugadores']}"
    return HttpResponse(respuesta)