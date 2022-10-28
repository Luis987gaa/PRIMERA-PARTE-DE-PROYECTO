from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime, timezone

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_parterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField()
    edad_actual: datetime

    def obtener_edad(self):
        edad_obtenida = datetime.now(tz=timezone.utc) - self.fecha_nacimiento 
        self.edad_actual = round(edad_obtenida.days / 365)

    def __str__(self):
        return f'{self.nombre}'