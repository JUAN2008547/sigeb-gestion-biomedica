from django import forms
from .models import EquipoMedico, Mantenimiento, Incidencia

class EquipoMedicoForm(forms.ModelForm):
    class Meta:
        model = EquipoMedico
        fields = [
            'nombre', 'marca', 'modelo', 'numero_serie', 
            'registro_invima', 'ubicacion', 
            'fecha_ultimo_mantenimiento', 'fecha_proximo_mantenimiento', 'imagen'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Defibrilador Bifásico'}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Zoll'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: R Series'}),
            'numero_serie': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: DEF-2026-089'}),
            'registro_invima': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 2021EBC-0001234'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Urgencias - Sala 2'}),
            'fecha_ultimo_mantenimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_proximo_mantenimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['equipo', 'tipo', 'fecha_mantenimiento', 'tecnico_responsable', 'costo', 'estado', 'observaciones']
        widgets = {
            'equipo': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'fecha_mantenimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tecnico_responsable': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del técnico o ingeniero'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalles del trabajo realizado...'}),
        }

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = ['equipo', 'titulo', 'prioridad', 'estado', 'descripcion']
        widgets = {
            'equipo': forms.Select(attrs={'class': 'form-select'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Falla en sensor de SpO2'}),
            'prioridad': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe detalladamente el fallo reportado...'}),
        }