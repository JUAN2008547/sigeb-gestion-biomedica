from django.shortcuts import render
from .models import EquipoMedico, Mantenimiento, Incidencia
from django.db.models import Q

def lista_equipos(request):
    equipos = EquipoMedico.objects.all()
    return render(request, 'equipos/lista_equipos.html', {'equipos': equipos})

def inventario(request):
    busqueda = request.GET.get('q', '')
    if busqueda:
        equipos = EquipoMedico.objects.filter(
            Q(nombre__icontains=busqueda) | 
            Q(marca__icontains=busqueda) | 
            Q(numero_serie__icontains=busqueda)
        )
    else:
        equipos = EquipoMedico.objects.all()
    return render(request, 'equipos/inventario.html', {'equipos': equipos, 'busqueda': busqueda})

def mantenimientos(request):
    busqueda = request.GET.get('q', '')
    if busqueda:
        lista_mantenimientos = Mantenimiento.objects.select_related('equipo').filter(
            Q(equipo__nombre__icontains=busqueda) |
            Q(tecnico_responsable__icontains=busqueda) |
            Q(tipo__icontains=busqueda)
        ).order_by('-fecha_mantenimiento')
    else:
        lista_mantenimientos = Mantenimiento.objects.select_related('equipo').all().order_by('-fecha_mantenimiento')
        
    return render(request, 'equipos/mantenimientos.html', {
        'mantenimientos': lista_mantenimientos, 
        'busqueda': busqueda
    })

def incidencias(request):
    busqueda = request.GET.get('q', '')
    if busqueda:
        lista_incidencias = Incidencia.objects.select_related('equipo').filter(
            Q(titulo__icontains=busqueda) |
            Q(equipo__nombre__icontains=busqueda)
        ).order_by('-fecha_reporte')
    else:
        lista_incidencias = Incidencia.objects.select_related('equipo').all().order_by('-fecha_reporte')

    return render(request, 'equipos/incidencias.html', {
        'incidencias': lista_incidencias, 
        'busqueda': busqueda
    })