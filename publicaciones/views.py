from django.shortcuts import render
from publicaciones.models import Publicacion
from .forms import PublicacionForm
from django.urls import reverse

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
# Create your views here.

"""def seguir_leyendo(request):
    template_name = "publicaciones/publicacion.html"
    contexto = {
        'info': publicacion.objects.all()
    }
    return render(request,template_name,contexto)"""


class AdminListaPublicaciones(ListView):
    template_name = 'listado_publicaciones.html'
    model = Publicacion
    context_object_name ="publicaciones"
    paginate_by = 2
    def get_queryset(self):
        publicaciones = Publicacion.objects.all()
        titulo_publicacion = self.request.GET.get("buscador")
        if titulo_publicacion:
            publicaciones = publicaciones.filter(titulo__contains=titulo_publicacion)

        return publicaciones.order_by("titulo")

class EditarPublicacion(UpdateView):
    model = Publicacion
    template_name = "editar.html"
    form_class = PublicacionForm
    def get_success_url(self):
        return reverse("publicacion:listado")


class NuevaPublicacion(CreateView):
    model = Publicacion
    template_name = "agregar_publicacion.html"
    form_class = PublicacionForm

    def get_success_url(self):
        return reverse("inicio")

class EliminarPublicacion(DeleteView):
    # specify the model you want to use
    model = Publicacion
    template_name = "eliminar.html"
    def get_success_url(self):
        return reverse("publicacion:listado")
    
""" asda def listado_publicaciones(request):
    template_name = 'listado_publicaciones.html'
    contexto = {
        'publicaciones': Publicacion.objects.all()
    }
    return render(request,template_name,contexto)sdas"""
    
def agregar_publicacion(request):
    template_name = "agregar_publicacion.html"
    contexto = {
        #'publicacion': publicacion.objects.all()
    }
    return render(request,template_name,contexto)

def publicacion(request):
    template_name = 'publicacion.html'
    contexto = {
    }
    return render(request, template_name, contexto)

