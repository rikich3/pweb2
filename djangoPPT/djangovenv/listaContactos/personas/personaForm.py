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
  def clean_nombre(self, *args, **kwargs):
    name = self.cleaned_data.get('nombre')
    if name == 'admin':
      raise forms.ValidationError('Invalid name')
    if not name.istitle():
      raise forms.ValidationError('Name must start with a capital letter')
    return name
    