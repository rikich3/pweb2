from django.shortcuts import render

# Create your views here.
def inspectPersona(request):
  myContext = {
    'id' : id,
    'Persona': ['nombre', 'apellido', 'edad', 'donador'],
  }
  return render(request, 'persona.html', myContext)