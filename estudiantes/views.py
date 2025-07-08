from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Estudiante
from .serializers import EstudianteSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    filter_fields = ['genero', 'procedencia', 'salud']