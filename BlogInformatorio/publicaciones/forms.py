from django import forms
from .models import Publicacion
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

		widgets = { 
			"nombre": forms.TextInput(attrs={"class": "form-control" }),
			"Body": forms.Textarea(attrs={"class": "form-control"}),
		}
