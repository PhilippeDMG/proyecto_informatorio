from django.db import models
from categorias.models import Categoria
# Create your models here.


class Publicacion(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=100)
    #categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)#null=True hace que las publicaciones ya cargadas tengan categoria null
    categoria = models.ManyToManyField(Categoria)
    imagen = models.ImageField(upload_to="publicaciones", default=True)
    def __str__(self):
        return self.titulo