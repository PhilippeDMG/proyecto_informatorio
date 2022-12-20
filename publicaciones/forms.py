from django import forms
from .models import Publicacion, Comentario
"""from django.db.models.fields import CommaSeparatedIntegerField
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario
"""

class PublicacionForm(forms.ModelForm):
	 

	class Meta:
		model = Publicacion
		fields= '__all__'
"""
		widgets = { 
			"nombre": forms.TextInput(attrs={"class": "form-control" }),
			"Body": forms.Textarea(attrs={"class": "form-control"}),
		}


class NuevoComentario(forms.ModelForm):
	
	class Meta:
		model = Comentario
		fields= ( "name", "body")
		widgets = {
			"name": forms.TextInput(attrs={"class": "col-sm-12"}),
		    "body": forms.Textarea(attrs={"class": "col-sm-12"}),

		}"""
