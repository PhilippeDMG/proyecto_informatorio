from django.urls import path
from . import views

app_name='publicacion'

urlpatterns = [
    #path('seguir_leyendo',views.seguir_leyendo),
    path('publicacion/<int:pk>',views.publicacion, name="publicacion"),
    path('listado_publicacion/',views.AdminListaPublicaciones.as_view(), name="listado"),
    path('agregar_publicacion/',views.NuevaPublicacion.as_view(),name="agregar"),
    path('editar/<int:pk>',views.EditarPublicacion.as_view(),name="editar"),
    path('eliminar/<int:pk>',views.EliminarPublicacion.as_view(),name="eliminar"),
    path('agregar_comentario/',views.AgregarComentario,name="agregar_comentario"),
]
#<in:pk> es el parámetro que recibe la view y pk es el valor por default que toma una view
 
