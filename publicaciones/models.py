from django.db import models

# Create your models here.


class Publicacion(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=100)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()