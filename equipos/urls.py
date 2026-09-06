from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_equipos, name='lista_equipos'),
    path('inventario/', views.inventario, name='inventario'),
    path('mantenimientos/', views.mantenimientos, name='mantenimientos'),
    path('incidencias/', views.incidencias, name='incidencias'),
]