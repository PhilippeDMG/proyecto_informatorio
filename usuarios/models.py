from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class usuario(AbstractUser):
    nombre = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    
