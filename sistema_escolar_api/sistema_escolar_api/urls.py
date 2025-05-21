"""point_experts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistema_escolar_api.views import alumnos, bootstrap, maestros, eventos
from sistema_escolar_api.views import users
from sistema_escolar_api.views import auth

urlpatterns = [
    #Version
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    #Create Admin
        path('admin/', users.AdminView.as_view()),
    #Admin Data
        path('lista-admins/', users.AdminAll.as_view()),
    #Edit Admin
        path('admins-edit/', users.AdminsViewEdit.as_view()),
    #Create Alumno
        path('alumnos/', alumnos.AlumnoView.as_view()),
    #Alumno Data
        path('lista-alumnos/', alumnos.AlumnosALL.as_view()),
    #Edit Alumno
        path('alumnos-edit/', alumnos.AlumnosViewEdit.as_view()),
    #Create Maestro
        path('maestros/', maestros.MaestroView.as_view()),
    #Maestro Data
        path('lista-maestros/', maestros.MaestrosAll.as_view()),
    #Edit Maestros
        path('maestros-edit/', maestros.MaestrosViewEdit.as_view()),
    #Create Evento
        path('eventos/', eventos.EventoView.as_view()),
    #Evento Data
        path('lista-eventos/', eventos.EventosAll.as_view()),
    #Edit Admin
        path('eventos-edit/', eventos.EventosViewEdit.as_view()),
    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view())
]
