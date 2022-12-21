from .models import Categoria
from django.views.generic.edit import CreateView
from .forms import NuevaCategoria
from django.urls import reverse
# Create your views here.

class NuevaCategoria(CreateView):
    model = Categoria
    template_name = "agregar_categoria.html"
    form_class = NuevaCategoria

    def get_success_url(self):
        return reverse("inicio")