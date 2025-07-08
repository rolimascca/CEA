from rest_framework import viewsets
from .models import Alergia, Enfermedad
from .serializers import AlergiaSerializer, EnfermedadSerializer

class AlergiaViewSet(viewsets.ModelViewSet):
    queryset = Alergia.objects.all()
    serializer_class = AlergiaSerializer
    filterset_fields = ['tipo']  # Usar filterset_fields requiere django-filter

class EnfermedadViewSet(viewsets.ModelViewSet):
    queryset = Enfermedad.objects.all()
    serializer_class = EnfermedadSerializer
