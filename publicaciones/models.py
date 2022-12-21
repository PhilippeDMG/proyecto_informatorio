from django.db import models
from categorias.models import Categoria
from users.models import Usuario
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


class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, related_name="comentarios", on_delete = models.CASCADE,default=True)
    usuario = models.ForeignKey(Usuario, related_name="comentarios", on_delete = models.CASCADE,default=True)
    #name = models.CharField(max_length=255,default=True)
    contenido = models.TextField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    """class Meta: 
		ordering = ("date_added",)
"""

    def __str__(self):
        return '%s - %s- %s' % (self.publicacion.titulo, self.usuario.first_name,self.usuario.last_name)
