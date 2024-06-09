from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request):
    return HttpResponse('<h1>Home</h1>')

def anotherView(request):
    return HttpResponse('<h1>Another Page</h1>')
