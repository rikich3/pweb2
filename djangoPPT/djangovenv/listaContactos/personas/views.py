from django.shortcuts import render
from .models import Persona

# Create your views here.
def inspectPersona(request):
  id = request.GET.get('id', '0')
  person = Persona.objects.get(id=id)
  myContext = {
    'id' : id,
    'Persona': person
  }
  return render(request, 'personas/persona.html', myContext)