from django.urls import path
from . import views

app_name='comentario'

urlpatterns = [
    path('agregar_comentario/',views.AgregarComentario,name="agregar_comentario"),
]
#<in:pk> es el parámetro que recibe la view y pk es el valor por default que toma una view
 
