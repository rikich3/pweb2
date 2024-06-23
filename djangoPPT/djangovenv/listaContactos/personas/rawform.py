import django.forms as forms

class RawPersonaForm(forms.Form):
  nombres = forms.CharField()
  apellidos = forms.CharField()
  donador = forms.BooleanField()
  edad = forms.IntegerField()