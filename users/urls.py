from django.urls import path
from . import views

app_name='usuarios'

urlpatterns = [
    path('registrarse/',views.Registrarse.as_view(), name="registrarse"),
]
