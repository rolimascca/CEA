from django.db import models
from estudiantes.models import Estudiante

class Alergia(models.Model):
    TIPO_ALERGIA = [
        ('alimentos', 'Alimenticias'),
        ('medicamentos', 'Medicamentos'),
        ('ambiental', 'Ambientales'),
    ]
    
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_ALERGIA)
    descripcion = models.TextField()

class Enfermedad(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='enfermedades_medical')
    nombre = models.CharField(max_length=100)
    es_cronica = models.BooleanField(default=False)
    otros = models.TextField(blank=True)  # Esta línea debe ir aquí, dentro del modelo

class HistorialMedico(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)
    grupo_sanguineo = models.CharField(max_length=10)
    cirugias = models.TextField(blank=True)
    problemas_psicologicos = models.TextField(blank=True)
    intolerancias = models.TextField(blank=True)
