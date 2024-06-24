from django.contrib import admin
from django.urls import path, include
from .views import PersonaListView

urlpatterns = [
  path('', PersonaListView.as_view(), name='personas_list'),
]
