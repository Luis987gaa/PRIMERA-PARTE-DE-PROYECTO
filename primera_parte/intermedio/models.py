from django.db import models

# Create your models here.

class Farmaco(models.Model):
    nombre = models.CharField(max_length=100)
    principio_activo = models.CharField(max_length=100)
    usos = models.CharField(max_length=100)
    tratamiento = models.TextField()

class Enfermedad(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    sintoma = models.TextField()
    clasificacion = models.CharField(max_length=100)

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_sangre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)