from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

@api_view(['GET'])
def reporte_medico(request):
    estudiantes = requests.get('http://localhost:8000/api/estudiantes/').json()
    enfermedades = requests.get('http://localhost:8000/api/medical/enfermedades/').json()
    
    data = {
        'total_estudiantes': len(estudiantes),
        'con_enfermedades': len([e for e in enfermedades if e['es_cronica']]),
    }
    return Response(data)

def reportes_html(request):
    return render(request, 'reportes/index.html')
