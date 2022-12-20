from django.shortcuts import render
#from django.shortcuts import redirect

from publicaciones.models import Publicacion

def inicio(request):
    
    template_name = 'inicio.html'
 
    contexto = {
        #'usuario': usuario.objects.all().filter( --- "username?"  ---)
        'publicaciones': Publicacion.objects.all(),
    }
    return render(request, template_name, contexto)

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

