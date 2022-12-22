from django import forms
from .models import Comentarios

class NuevoComentario(forms.ModelForm):
    def __init__(self, args, **kwargs):
        super().__init__(args, **kwargs)
        self.fields['contenido'].widget.attrs.update({'rows': '3'})
    class Meta:
        model = Comentarios
        fields= ['contenido']
        """widgets = {
            "name": forms.TextInput(attrs={"class": "col-sm-12"}),
            "body": forms.Textarea(attrs={"class": "col-sm-12"}),
    }"""
