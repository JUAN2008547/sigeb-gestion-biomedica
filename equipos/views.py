from django.shortcuts import render
from .models import EquipoMedico, Mantenimiento
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
    lista_mantenimientos = Mantenimiento.objects.select_related('equipo').all().order_by('-fecha_mantenimiento')
    return render(request, 'equipos/mantenimientos.html', {'mantenimientos': lista_mantenimientos})