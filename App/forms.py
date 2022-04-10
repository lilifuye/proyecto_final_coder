from django import forms

class JugadoresFormulario(forms.Form):
    nombre = forms.CharField()    
    edad = forms.IntegerField()               
    nivel = forms.IntegerField()       