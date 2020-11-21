from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def registrarse(request):
    context={}
    return render(request,'miAplicacion/registrarUsuario.html',context)

def datosUsuario(request):
    nombre = request.POST['nombre']
    correo = request.POST['email']
    fechaN = request.POST['fechaN']
    return render(request,'miAplicacion/datosUsuario.html',{'name':nombre,'email':correo,'date':fechaN})

# Create your views here.
