from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


class Administradores(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave_admin = models.CharField(max_length=255,null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    ocupacion = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del admin "+self.first_name+" "+self.last_name
    
#TODO: A partir de aquí deben de definir ustedes sus modelos para alumnos y maestros

class Alumnos(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave_alumno = models.CharField(max_length=255,null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    curp = models.CharField(max_length=255,null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    ocupacion = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del alumno "+self.first_name+" "+self.last_name
    
class Maestros(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    clave_maestro = models.CharField(max_length=255,null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    curp = models.CharField(max_length=255,null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    cubiculo = models.CharField(max_length=255,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    area_investigacion = models.CharField(max_length=255,null=True, blank=True)
    materias_json = models.TextField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del maestro "+self.first_name+" "+self.last_name
    
class Evento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_evento = models.CharField(max_length=255)
    tipo_evento = models.CharField(max_length=255)
    fecha_evento = models.DateTimeField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_final = models.TimeField(null=True, blank=True)
    lugar = models.CharField(max_length=255)
    publico_json = models.TextField(null=True, blank=True)
    programa_educativo = models.CharField(max_length=255, null=True, blank=True)
    responsable_evento = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField()
    cupo = models.PositiveIntegerField(null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "El nombre del evento es "+self.nombre_evento