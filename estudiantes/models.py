from django.db import models

# Create your models here.
class Estudiante(models.Model):
    GENERO = [('V', 'Varón'), ('M', 'Mujer')]
    
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    genero = models.CharField(max_length=1, choices=GENERO)
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=15, unique=True)
    procedencia = models.CharField(max_length=100)
    direccion = models.TextField()
    celular = models.CharField(max_length=20, blank=True)
    
    padre = models.CharField(max_length=100, blank=True)
    madre = models.CharField(max_length=100, blank=True)
    apoderado = models.CharField(max_length=100, blank=True)
    
    vive_con = models.CharField(max_length=100)
    total_personas_hogar = models.IntegerField()
    
    salud = models.CharField(max_length=50)
    enfermedad_actual = models.BooleanField(default=False)
    enfermedad_desc = models.TextField(blank=True)
    atencion_psicologica = models.BooleanField(default=False)
    psicologico_desc = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"