from django.shortcuts import render

def inicio(request):
    template_name = 'inicio.html'
    contexto = {
    }
    return render(request, template_name, contexto)

def iniciar_sesion(request):
    if request.method == "POST": 
        data = request.POST.get('boton')
        print(data)
    contexto = {
    }
    return render(request, 'iniciar_sesion.html', contexto)
def registrarse(request):
    template_name = 'registrarse.html'
    contexto = {
    }
    return render(request, template_name, contexto)
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

    


      