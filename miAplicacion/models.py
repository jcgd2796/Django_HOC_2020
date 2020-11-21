from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    fechaNacimiento = models.DateTimeField('Fecha de nacimiento')
    email = models.EmailField(max_length=200)

# Create your models here.
