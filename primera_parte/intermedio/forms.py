from django import forms

class PacienteForm(forms.Form):
    nombre = forms.CharField(label='Nombre del paciente ', max_length=100)
    tipo_sangre = forms.CharField(label='Tipo de sangre ', max_length=5)
    nacionalidad = forms.CharField(label='Nacionalidad ', max_length=10)
    
class FarmacoForm(forms.Form):
    nombre = forms.CharField(label='Nombre del fármaco ', max_length=100)
    principio_activo = forms.CharField(label='Principio activo ', max_length=100)
    usos = forms.CharField(label='Usos e indicaciones ', max_length=100)
    tratamiento = forms.CharField(label='Tiempo de Tratamiento ', max_length=100)
    
class EnfermedadForm(forms.Form):
    nombre = forms.CharField(label='Enfermedad ', max_length=100)
    tipo = forms.CharField(label='Etapa o tipo ', max_length=100)
    sintoma = forms.CharField(label='Síntomas ', max_length=300)
    clasificacion = forms.CharField(label='Clasificación ', max_length=100)
    