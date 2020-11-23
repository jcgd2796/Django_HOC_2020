from django.shortcuts import render
from django.http import HttpResponse
from miAplicacion.models import Usuario

def index(request):
    return HttpResponse("Hello world")

def registrarse(request):
    context={}
    return render(request,'miAplicacion/registrarUsuario.html',context)

def datosUsuario(request):
    nombr = request.POST['nombre']
    em = request.POST['email']
    fn = request.POST['fechaN']
    usuario = Usuario(nombre = nombr,fechaNacimiento = fn,email = em)
    usuario.save()
    return render(request,'miAplicacion/datosUsuario.html',{'name':nombr,'email':em,'date':fn})

def getUsuario(request):
    return render(request,'miAplicacion/buscarUsuario.html',{})

def buscarUsuario(request):
    ident = request.POST['id']
    u = Usuario.objects.get(id = ident)
    nombr = u.nombre
    em = u.email
    fn = u.fechaNacimiento
    return render(request,'miAplicacion/datosUsuario.html',{'name':nombr,'email':em,'date':fn})

# Create your views here.
