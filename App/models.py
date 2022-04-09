from django.db import models

# Create your models here.

class jugadores(models.Model):
    nombre = models.CharField(max_length=50)    
    edad = models.IntegerField()               
    nivel = models.IntegerField()               

class entrenadores(models.Model):
    nombre = models.CharField(max_length=50)    
    edad = models.IntegerField()
    equipo = models.CharField(max_length=50)            


class sponsors(models.Model):
    nombre = models.CharField(max_length=50)    
    edad = models.IntegerField()
    producto = models.CharField(max_length=50)                