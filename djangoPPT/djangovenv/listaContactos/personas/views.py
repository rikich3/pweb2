from django.shortcuts import render
from .models import Persona
from .personaForm import PersonaForm

# Create your views here.
def inspectPersona(request):
  id = request.GET.get('id', '0')
  person = Persona.objects.get(id=id)
  myContext = {
    'id' : id,
    'Persona': person
  }
  return render(request, 'personas/persona.html', myContext)
def addPersona(request):
  form = PersonaForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = PersonaForm()
  addContext = {
    'form': form
  }
  return render(request, 'personas/addPersona.html', addContext)