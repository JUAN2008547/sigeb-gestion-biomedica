from django.shortcuts import render
from .models import Incidencia

def lista_incidencias(request):
    incidencias = Incidencia.objects.all().order_by('-fecha_reporte')
    return render(request, 'incidencias/incidencias.html', {'incidencias': incidencias})