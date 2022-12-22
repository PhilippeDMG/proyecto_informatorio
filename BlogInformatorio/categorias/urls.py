from django.urls import path
from . import views

app_name='categorias'

urlpatterns = [
    path('agregar_categoria/',views.NuevaCategoria.as_view(), name="agregar_categoria"),
]
#<in:pk> es el parámetro que recibe la view y pk es el valor por default que toma una view
 
