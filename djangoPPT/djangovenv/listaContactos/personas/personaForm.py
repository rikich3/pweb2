from django import forms
from .models import Persona
class PersonaForm(forms.ModelForm):
  class Meta:
    model = Persona
    fields = ['nombre', 'apellidos', 'edad', 'donador', 'correo']
    labels = {
      'nombre': 'Nombre',
      'apellidos': 'Apellidos',
      'edad': 'Edad',
      'donador': '¿Es donador?',
      'correo': 'Correo electrónico'
    }