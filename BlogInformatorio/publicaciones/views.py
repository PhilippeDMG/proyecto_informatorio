from django.shortcuts import render
from publicaciones.models import Publicacion
from comentarios.models import Comentarios
from categorias.models import Categoria
from .forms import PublicacionForm
from comentarios.forms import NuevoComentario
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from utils.mixins import IsAdminMixin
# Create your views here.

class AdminListaPublicaciones(LoginRequiredMixin, IsAdminMixin,ListView):
    template_name = 'listado_publicaciones.html'
    model = Publicacion
    context_object_name ="publicaciones"
    paginate_by = 6
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
    
"""
def pub(request):
    pub = Publicacion.objects.get(all)
    return render(pub)

def ExistePost(id):
    for i in pub:
        if i.id == id:
            return i
    return None

def ReadPost(request, id):
	try:
		posts   = ExistePost(id)
	except Exception:
		posts   = Publicacion.objects.get(id=id)
	comentarios = Comentario.objects.filter(pub=id)

	form = NuevoComentario(request.POST or None)
	if form.is_valid():
		if request.user.is_authenticated:
			aux         =  form.save(commit=False)
			aux.noticia = posts
			aux.user    = request.user
			aux.save()
			form        = NuevoComentario()
		else:
			return redirect('login')
	context = {
		'titulo': 'publicacion',
		'posts': posts,
		'form': form,
		'comentarios': comentarios,
	}
	return render(request,'publicacion.html', context)
    
"""

def publicaciones(request):
    publicaciones = Publicacion.objects.get(all)
    return render(publicaciones)

def ExistePost(id):
    for i in publicaciones:
        if i.id == id:
            return i
    return None

	

def publicacion(request,id):
    try:
        publicacion   = ExistePost(id)
    except Exception:
        publicacion  = Publicacion.objects.get(id=id)
    comentarios = Comentarios.objects.filter(publicacion=id)
    template_name = 'publicacion.html'
    form = NuevoComentario(request.POST or None)
    if form.is_valid():
        aux         =  form.save(commit=False)
        aux.publicacion = publicacion
        aux.usuario    = request.user
        aux.save()
        form        = NuevoComentario()

    categorias = Categoria.objects.all()
    contexto = { 'publicacion': publicacion,
                'comentarios': comentarios,
                'form': form,
                'categorias': categorias,
    }
    return render(request, template_name, contexto)


def filtro_categoria(request,categoria):
    filtro = Categoria.objects.filter(nombre=categoria)
    publicacion    = Publicacion.objects.filter(categoria=filtro[0].id)
    categorias  = Categoria.objects.all()
    template_name='filtro_categoria.html'
    context    = {
        'publicaciones' : publicacion,
        'categorias':categorias
    }
    return render(request,template_name,context)

