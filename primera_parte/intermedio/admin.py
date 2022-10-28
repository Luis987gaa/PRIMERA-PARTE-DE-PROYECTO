from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Paciente)
admin.site.register(models.Farmaco)
admin.site.register(models.Enfermedad)
