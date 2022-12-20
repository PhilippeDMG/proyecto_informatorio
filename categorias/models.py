from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre