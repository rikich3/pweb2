import django.forms as forms

class RawPersonaForm(forms.Form):
  nombres = forms.CharField(
    widget=forms.Textarea(
      attrs={
        'placeholder': 'Your name',
        'class': 'form-control',
        'id': 'nombres'
      }
    )
  )
  apellidos = forms.CharField()
  donador = forms.BooleanField()
  edad = forms.IntegerField()