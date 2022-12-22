from django.db import models
from users.models import Usuario
from publicaciones.models import Publicacion
from django.conf import settings
# Create your models here.

class Comentarios(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,default=Usuario)
    publicacion = models.ForeignKey(Publicacion, on_delete = models.CASCADE)
    
    #name = models.CharField(max_length=255,default=True)
    contenido = models.TextField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    class Meta: 
        ordering = ("fecha_agregado",)


    def __str__(self):
        return '%s - %s- %s' % (self.publicacion.titulo, self.usuario.first_name,self.usuario.last_name)
