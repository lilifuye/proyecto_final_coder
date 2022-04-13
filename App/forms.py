from django import forms

class JugadoresFormulario(forms.Form):
    nombre = forms.CharField()    
    edad = forms.IntegerField()               
    nivel = forms.IntegerField()       

class EntrenadoresFormulario(forms.Form):
    nombre = forms.CharField()    
    edad = forms.IntegerField()               
    equipo = forms.CharField()    

class SponsorsFormulario(forms.Form):
    nombre = forms.CharField()    
    edad = forms.IntegerField()               
    producto = forms.CharField()    