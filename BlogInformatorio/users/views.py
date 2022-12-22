from django.shortcuts import render
from django.views.generic import CreateView
from users.models import Usuario
from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm
# Create your views here.

class Registrarse(CreateView):
    model         = Usuario
    form_class    = RegistroUsuarioForm
    template_name = 'registrarse.html'
    success_url   = reverse_lazy('inicio')