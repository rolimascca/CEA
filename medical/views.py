from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Alergia, Enfermedad
from .serializers import AlergiaSerializer, EnfermedadSerializer

class AlergiaViewSet(viewsets.ModelViewSet):
    queryset = Alergia.objects.all()
    serializer_class = AlergiaSerializer
    filter_fields = ['tipo']

class EnfermedadViewSet(viewsets.ModelViewSet):
    queryset = Enfermedad.objects.all()
    serializer_class = EnfermedadSerializer