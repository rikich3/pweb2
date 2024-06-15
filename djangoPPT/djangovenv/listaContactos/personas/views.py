from django.shortcuts import render

# Create your views here.
def inspectPersona(request):
  myContext = {
    'Persona': ['nombre', 'apellido', 'edad', 'donador'],
  }
  return render(request, 'persona.html', myContext)