from django.shortcuts import render
from .forms import NuevoComentario
from users.models import Usuario
# Create your views here.

def AgregarComentario(request):
	usuario = Usuario(usuario=request.user)
	form = NuevoComentario(request.POST or None)
	if form.is_valid():
		form.save()
		form = NuevoComentario()
	
	context={
		'form': form,
		'usuario': usuario,
	}
	return render(request,'agregar_comentario.html', context)
 
