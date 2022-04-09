from django.shortcuts import render
from .models import *
# Create your views here.

def inicio(request):
    return render (request,'App/inicio.html')
   
def jugadores(request):
    return render (request, 'App/jugadores.html')

def entrenadores(request):
    return render (request, 'App/entrenadores.html')

def sponsors(request):
    return render (request, 'App/sponsors.html')