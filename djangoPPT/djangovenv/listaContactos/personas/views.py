from django.shortcuts import get_object_or_404, render
from .models import Persona
from .personaForm import PersonaForm, RawPersonaForm

# Create your views here.
def createUpdatePersona(request):
  form = RawPersonaForm()
  if(request.method == 'POST'):
    firstPerson = Persona.objects.first()
    form = RawPersonaForm(request.POST, instance = firstPerson)
    if form.is_valid():
      form.save()
      form = RawPersonaForm()
    else:
      print(form.errors)
  context = {
    'form': form
  }
  return render(request, 'personas/createUpdatePersona.html', context)
def UpdatePersona(request, miID):
  firstPerson = Persona.objects.get(id = miID)
  form = RawPersonaForm(request.POST, instance = firstPerson)
  if(request.method == 'POST'):
    if form.is_valid():
      form.save()
      form = RawPersonaForm()
    else:
      print(form.errors)
  context = {
    'form': form
  }
  return render(request, 'personas/createUpdatePersona.html', context)

def erasePersona(request, targetID):
  obj = get_object_or_404(Persona, id = targetID)
  if request.method == 'POST':
    obj.delete()
  context = {
    'object': obj
  }
  return render(request, 'personas/confirmDelete.html', context)

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
def searchPersona(request):
  if request.method == 'POST':
    form = PersonaForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        try:
            persona = Persona.objects.get(nombre=name)
            return render(request, 'persona_detail.html', {'persona': persona})
        except Persona.DoesNotExist:
            error_message = "Persona with name '{}' does not exist.".format(name)
            return render(request, 'search_persona.html', {'form': form, 'error_message': error_message})
    else:
        form = PersonaForm()

  return render(request, 'personas/searchPersona.html')