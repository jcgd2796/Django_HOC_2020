from django.urls import path
from . import views

urlpatterns=[
        path('',views.index,name="Página principal"),
        path('registrarse',views.registrarse),
        path('datosUsuario',views.datosUsuario),
        ]

