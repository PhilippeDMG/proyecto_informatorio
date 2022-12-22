from users.models import Usuario
from django.db import transaction
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistroUsuarioForm(UserCreationForm):
    #redefinir el widget (html tag)
    first_name = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={"class": "forms control"}))
    last_name = forms.CharField(label='Apellido',widget=forms.TextInput(attrs={"class": "forms control"}))

    class Meta:
        model  = Usuario
        fields = ['first_name','last_name','username','password1','password2','email']

    @transaction.atomic
    def save(self):
        user              = super().save(commit=False)
        user.is_superuser = False
        user.is_staff     = False
        user.save()
        return user