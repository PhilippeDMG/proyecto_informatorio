from django.shortcuts import render, redirect
from publicaciones.models import Publicacion,Comentario
from .forms import PublicacionForm,NuevoComentario
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
# Create your views here.

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
    
def AgregarComentario(request):
	form = NuevoComentario(request.POST or None)
	if form.is_valid():
		form.save()
		form = NuevoComentario()
	
	context={
		'form': form,
	}
	return render(request,'agregar_comentario.html', context)
 

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
def publicacion(request,pk):
    
    template_name = 'publicacion.html'
    """SoloEstePost = None
    if request.method == 'POST':
        form_comentario = NuevoComentario(request.POST)
        if comment_form.is_valid():
            SoloEstePost = form_comentario.save(commit=False)
            SoloEstePost. = p
            SoloEstePost.save()
			
    else:
        comment_form = NuevoComentario()"""
    contexto = { 'publicacion': Publicacion.objects.get(pk = pk), 
    }
    return render(request, template_name, contexto)

