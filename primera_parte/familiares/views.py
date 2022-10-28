from django.shortcuts import render
from . import models

# Create your views here.

def vista_familiares(request):
    familiares = models.Familiares.objects.all()
    for familiar in familiares:
        familiar.obtener_edad()
    context = {
        'familiares': familiares,
        'titulo' : 'Familiares'
    }
    return render(request, 'lista_familiares.html', context )