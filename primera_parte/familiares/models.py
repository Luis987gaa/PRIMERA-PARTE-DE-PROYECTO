from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_parterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}'