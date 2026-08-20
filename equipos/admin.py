from django.contrib import admin
from .models import EquipoMedico, Mantenimiento

@admin.register(EquipoMedico)
class EquipoMedicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'modelo', 'numero_serie', 'ubicacion', 'fecha_proximo_mantenimiento')
    search_fields = ('nombre', 'numero_serie', 'marca', 'registro_invima')
    list_filter = ('marca', 'ubicacion')

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'tipo', 'fecha_mantenimiento', 'tecnico_responsable', 'estado', 'costo')
    list_filter = ('tipo', 'estado', 'fecha_mantenimiento')
    search_fields = ('equipo__nombre', 'tecnico_responsable')