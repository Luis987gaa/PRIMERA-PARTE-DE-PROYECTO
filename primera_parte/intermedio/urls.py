from django.urls import path
from .import views
urlpatterns = [
    path(route='', view=views.home_page, name='home'),
    path(route='agregar-paciente/', view=views.agregar_paciente, name='agregar_paciente'),
    path(route='agregar-enfermedad/', view=views.agregar_enfermedad, name='agregar_enfermedad'),
    path(route='agregar-farmaco/', view=views.agregar_farmaco, name='agregar_farmaco'),
]