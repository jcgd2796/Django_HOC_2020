from django.test import TestCase
from miAplicacion.models import Usuario
import datetime

class UsuarioTestCase(TestCase):
    #siempre comienzan con test_...
    def test_compruebaUsuarioCreado(self):
        usuariosActuales = Usuario.objects.all().count()
        Usuario.objects.create(nombre = "Jorge", fechaNacimiento= datetime.datetime.now(), email = "jorge@jorge.com")

        self.assertEqual(usuariosActuales+1,Usuario.objects.all().count())

    def test_compruebaDatosUsuarioCreado(self):
        Usuario.objects.create(nombre = "Jorge", fechaNacimiento= datetime.datetime.now(), email = "jorge@jorge.com")

        self.assertEqual("Jorge",Usuario.objects.get(nombre = "Jorge").nombre)
        self.assertEqual(datetime.datetime.now().day,Usuario.objects.get(nombre = "Jorge").fechaNacimiento.day)
        self.assertEqual("jorge@jorge.com",Usuario.objects.get(nombre = "Jorge").email)

    def test_setFechaNoValida(self):
        u = Usuario(nombre = "Alberto", fechaNacimiento = datetime.datetime.now(),email= "alberto@alberto.com")
        self.assertRaises(Exception, u.setFechaNacimiento,datetime.datetime(2021,11,25))

    def test_setFechaValida(self):
        u = Usuario(nombre = "Alberto", fechaNacimiento = datetime.datetime.now(),email= "alberto@alberto.com")
        u.setFechaNacimiento(datetime.datetime(2019,11,25))
        self.assertEqual(datetime.datetime(2019,11,25),u.fechaNacimiento)

# Create your tests here.
