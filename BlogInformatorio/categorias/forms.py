from django import forms
from .models import Categoria


class NuevaCategoria(forms.ModelForm):
	
	class Meta:
		model = Categoria
		fields= '__all__'
		"""widgets = {
			"name": forms.TextInput(attrs={"class": "col-sm-12"}),
		    "body": forms.Textarea(attrs={"class": "col-sm-12"}),
		}"""
