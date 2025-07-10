from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Alergia, Enfermedad
from .serializers import AlergiaSerializer, EnfermedadSerializer

class AlergiaViewSet(viewsets.ModelViewSet):
    queryset = Alergia.objects.all()
    serializer_class = AlergiaSerializer
    filterset_fields = ['tipo']  # Usar filterset_fields requiere django-filter

class EnfermedadViewSet(viewsets.ModelViewSet):
    queryset = Enfermedad.objects.all()
    serializer_class = EnfermedadSerializer



from medical.models import Alergia

@api_view(['GET'])
def estudiantes_por_alergia(request, tipo_alergia):
    estudiantes = Alergia.objects.filter(tipo=tipo_alergia).select_related('estudiante')
    data = {
        'tipo_alergia': tipo_alergia,
        'estudiantes': [
            {
                'id': alergia.estudiante.id,
                'nombre': f"{alergia.estudiante.nombre} {alergia.estudiante.apellido}",
                'descripcion': alergia.descripcion,
            }
            for alergia in estudiantes
        ]
    }
    return render(request, 'reportes/filtro.html', context=data)