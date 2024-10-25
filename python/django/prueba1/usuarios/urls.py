# clase utilizada para guardar la url de nuestra app usuarios

from django.urls import path
from . import views

urlpatterns = [path('formulario/', views.guardar_datos, name='guardar_datos')]