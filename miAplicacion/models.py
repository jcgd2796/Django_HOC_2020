from django.db import models
import datetime

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    fechaNacimiento = models.DateTimeField('Fecha de nacimiento')
    email = models.EmailField(max_length=200)

    #def __init__(self, name, fn, em):
     #   self.nombre = name
      #  self.fechaNacimiento = fn
       # self.email = em

    def __str__(self):
        return self.email

    def setNombre(self,nuevo):
        if nuevo != "" and nuevo != None:
            self.nombre = nuevo
        else:
            raise Exception("El nombre está vacio o es None")

    def setFechaNacimiento(self,nueva):
        if nueva < datetime.datetime.now() and nueva != None:
            self.fechaNacimiento = nueva
        else:
            raise Exception("Fecha no válida")

    def setEmail(self,nuevo):
        if nuevo !="" and nuevo != None:
            self.email = nuevo
        else:
            raise Exception("Email no valido")



# Create your models here.
