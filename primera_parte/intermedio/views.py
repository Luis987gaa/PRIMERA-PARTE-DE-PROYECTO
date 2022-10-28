from django.shortcuts import render, redirect
from . import forms 
from . import models
# Create your views here.

def home_page(request):
    pacientes = models.Paciente.objects.all()
    enfermedades = models.Enfermedad.objects.all()
    farmacos = models.Farmaco.objects.all()
    context = {
        'gato': '🦷''✨''🐈',
        'pacientes': pacientes,
        'enfermedades': enfermedades,
        'farmacos': farmacos
    }
    return render(request=request , template_name= 'tablas.html', context=context)

"""" DATOS DEL PACIENTE """

def agregar_paciente(request):
    if request.method == 'POST':
        paciente_formulario = forms.PacienteForm(request.POST)
        if paciente_formulario.is_valid():
            info = paciente_formulario.cleaned_data
            paciente = models.Paciente(nombre=info['nombre'], 
            tipo_sangre=info['tipo_sangre'], 
            nacionalidad=info['nacionalidad'])
            paciente.save()
            return redirect(to='home')
    context = {
        'gato': '🦷''✨''🐈',
        'form': forms.PacienteForm()
    }
    return render(request=request, template_name='forms/formulario_paciente.html', context=context)

"""" DATOS DE LA ENFERMEDAD DEL PACIENTE """

def agregar_enfermedad(request):
    if request.method == 'POST':
        enfermedad_formulario = forms.EnfermedadForm(request.POST)
        if enfermedad_formulario.is_valid():
            info = enfermedad_formulario.cleaned_data
            enfermedad = models.Enfermedad(nombre=info['nombre'], 
            tipo=info['tipo'], 
            sintoma=info['sintoma'],
            clasificacion=info['clasificacion'])
            enfermedad.save()
            return redirect(to='home')
    context = {
        'gato': '🦷''✨''🐈',
        'form': forms.EnfermedadForm()
    }
    return render(request=request, template_name='forms/formulario_enfermedad.html', context=context)

"""" DATOS DEL TRATAMIENTO A SEGUIR """

def agregar_farmaco(request):
    if request.method == 'POST':
        farmaco_formulario = forms.FarmacoForm(request.POST)
        if farmaco_formulario.is_valid():
            info = farmaco_formulario.cleaned_data
            farmaco = models.Farmaco(nombre=info['nombre'], 
            principio_activo=info['principio_activo'], 
            usos=info['usos'],
            tratamiento=info['tratamiento'])
            farmaco.save()
            return redirect(to='home')
    context = {
        'gato': '🦷''✨''🐈',
        'form': forms.FarmacoForm()
    }
    return render(request=request, template_name='forms/formulario_farmaco.html', context=context)