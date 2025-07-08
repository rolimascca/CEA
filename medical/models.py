from django.db import models

# Create your models here.
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
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    es_cronica = models.BooleanField(default=False)

class HistorialMedico(models.Model):
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)
    grupo_sanguineo = models.CharField(max_length=10)
    cirugias = models.TextField(blank=True)
    problemas_psicologicos = models.TextField(blank=True)
    intolerancias = models.TextField(blank=True)
    otros = models.TextField(blank=True)