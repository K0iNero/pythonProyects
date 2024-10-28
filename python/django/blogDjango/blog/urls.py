from django.urls import path
from . import views

urlpatterns = [
    path('blogInicio/', views.listar_publicaciones, name='listar_publicaciones'),
    path('addPost/', views.agregar_publicacion, name='agregar_publicacion'),
    path('publicacion/<int:publicacion_id>/', views.ver_publicacion, name='ver_publicacion'),
    path('publicacion/<int:publicacion_id>/comentario/', views.agregar_comentario, name='agregar_comentario'),
]
