from django.urls import path
from . import views

urlpatterns = [
    # Vistas principales
    path('', views.lista_equipos, name='lista_equipos'),
    path('inventario/', views.inventario, name='inventario'),
    path('mantenimientos/', views.mantenimientos, name='mantenimientos'),
    path('incidencias/', views.incidencias, name='incidencias'),

    # Vistas para la creación de registros
    path('equipo/nuevo/', views.crear_equipo, name='crear_equipo'),
    path('mantenimiento/nuevo/', views.crear_mantenimiento, name='crear_mantenimiento'),
    path('incidencia/nueva/', views.crear_incidencia, name='crear_incidencia'),
]