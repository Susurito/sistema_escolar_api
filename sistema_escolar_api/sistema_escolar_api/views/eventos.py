from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from sistema_escolar_api.serializers import *
from sistema_escolar_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json


class EventosAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        eventos = Evento.objects.all().order_by("id")
        eventos = EventoSerializer(eventos, many=True).data
        if not eventos:
            return Response({}, 400)
        for evento in eventos:
            evento["publico_json"] = json.loads(evento["publico_json"])
        return Response(eventos, 200)

class EventoView(generics.CreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    # Obtener evento por ID
    def get(self, request, *args, **kwargs):
        evento = get_object_or_404(Evento, id=request.GET.get("id"))
        evento = EventoSerializer(evento, many=False).data
        evento["publico_json"] = json.loads(evento["publico_json"])
        return Response(evento, 200)

    # Registrar nuevo evento
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data["publico_json"] = json.dumps(data["publico_json"])

        evento = EventoSerializer(data=data)
        if evento.is_valid():
            evento = evento.save()
            return Response({"evento_created_id": evento.id}, 201)
        return Response(evento.errors, status=status.HTTP_400_BAD_REQUEST)

class EventosViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    #Editar evento
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        evento = get_object_or_404(Evento, id=request.data["id"])
        evento.nombre_evento = request.data["nombre_evento"]
        evento.tipo_evento = request.data["tipo_evento"]
        evento.fecha_evento = request.data["fecha_evento"]
        evento.hora_inicio = request.data["hora_inicio"]
        evento.hora_final = request.data["hora_final"]
        evento.lugar = request.data["lugar"]
        evento.publico_json = json.dumps(request.data["publico_json"])
        evento.programa_educativo = request.data["programa_educativo"]
        evento.responsable_evento = request.data["responsable_evento"]
        evento.descripcion = request.data["descripcion"]
        evento.cupo = request.data["cupo"]
        evento.save()
        user = EventoSerializer(evento, many=False).data

        return Response(user,200)
    
    #Eliminar evento
    def delete(self, request, *args, **kwargs):
        evento = get_object_or_404(Evento, id=request.GET.get("id"))
        try:
            evento.delete()
            return Response({"details":"Evento eliminado"},200)
        except Exception as e:
            return Response({"details":"Algo pasó al eliminar"},400)

