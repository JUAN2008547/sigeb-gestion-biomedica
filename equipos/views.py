from django.shortcuts import render, redirect
from .models import EquipoMedico, Mantenimiento, Incidencia
from .forms import EquipoMedicoForm, MantenimientoForm, IncidenciaForm
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

# --- VISTAS PARA CREAR REGISTROS DESDE LA INTERFAZ PROPIA ---

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoMedicoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = EquipoMedicoForm()
    return render(request, 'equipos/formulario_generic.html', {
        'form': form, 
        'titulo_pagina': 'Registrar Nuevo Equipo Médico',
        'subtitulo': 'Llena los campos para ingresar un dispositivo al inventario'
    })

def crear_mantenimiento(request):
    if request.method == 'POST':
        form = MantenimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mantenimientos')
    else:
        form = MantenimientoForm()
    return render(request, 'equipos/formulario_generic.html', {
        'form': form, 
        'titulo_pagina': 'Registrar Mantenimiento',
        'subtitulo': 'Ingresa los detalles del mantenimiento preventivo o correctivo'
    })

def crear_incidencia(request):
    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incidencias')
    else:
        form = IncidenciaForm()
    return render(request, 'equipos/formulario_generic.html', {
        'form': form, 
        'titulo_pagina': 'Reportar Nueva Incidencia',
        'subtitulo': 'Registra una falla detectada en un equipo biomédico'
    })