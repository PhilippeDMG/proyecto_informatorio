from django.shortcuts import render
#from django.shortcuts import redirect
from django.views.generic import ListView
from publicaciones.models import Publicacion
from categorias.models import Categoria

class inicio(ListView):
    template_name = 'inicio.html'
    model = Publicacion.objects.order_by('-fecha')
    context_object_name ="publicaciones"
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['categorias']=Categoria.objects.all()
        return contexto
    def get_queryset(self):
        publicaciones = Publicacion.objects.all()
        titulo_publicacion = self.request.GET.get("buscador")
        if titulo_publicacion:
            publicaciones = publicaciones.filter(titulo__contains=titulo_publicacion)

        return publicaciones.order_by("titulo")

"""
def inicio(request):
    
    template_name = 'inicio.html'
 
    contexto = {
        #'usuario': usuario.objects.all().filter( --- "username?"  ---)
        'publicaciones': Publicacion.objects.all(),
        'categorias': Categoria.objects.all(),
    }
    return render(request, template_name, contexto)
"""
def login(request):
    #Para que se muestren los prints tuve que cambiar en urls.py el path a views.iniciar_sesion, antes era algo similar a auth.views("iniciar_sesion.html")
    #print("holaaaa")
    #print(request.GET["username"])
    #if request.method == 'POST':
    #    form = (request.POST)

    return render(request, 'login.html', {})


"""def registrarse(request):
    form = UserCreationForm()
    template_name = 'registrarse.html'
    model = usuario
    if request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


    contexto = {'form':form}
    return render(request, template_name, contexto)"""


def comentar(request):
    template_name = 'comentar.html'
    contexto = {
    }
    return render(request, template_name, contexto)
def informacion(request):
    template_name = 'informacion.html'
    contexto = {
    }
    return render(request, template_name, contexto)

