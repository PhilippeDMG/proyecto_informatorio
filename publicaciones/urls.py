from django.urls import path
from . import views

app_name='publicacion'

urlpatterns = [
    path('publicacion/<int:id>',views.publicacion, name="publicacion"),
    path('listado_publicacion/',views.AdminListaPublicaciones.as_view(), name="listado"),
    path('agregar_publicacion/',views.NuevaPublicacion.as_view(),name="agregar"),
    path('editar/<int:pk>',views.EditarPublicacion.as_view(),name="editar"),
    path('eliminar/<int:pk>',views.EliminarPublicacion.as_view(),name="eliminar"),
    path('filtro_categoria/<str:categoria>',views.filtro_categoria, name='filtro_categoria'),
]
#<in:pk> es el parámetro que recibe la view y pk es el valor por default que toma una view
 
