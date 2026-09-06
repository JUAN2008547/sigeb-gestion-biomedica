from django.db import models

class EquipoMedico(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Equipo")
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50, unique=True, verbose_name="Número de Serie")
    registro_invima = models.CharField(max_length=50, verbose_name="Registro INVIMA")
    ubicacion = models.CharField(max_length=100, help_text="Ej: Consultorio 1, Sala de Procedimientos")
    fecha_ultimo_mantenimiento = models.DateField(verbose_name="Último Mantenimiento")
    fecha_proximo_mantenimiento = models.DateField(verbose_name="Próximo Mantenimiento")
    imagen = models.ImageField(upload_to='equipos/', blank=True, null=True, verbose_name="Fotografía del Equipo")

    def __str__(self):
        return f"{self.nombre} ({self.numero_serie})"

    class Meta:
        verbose_name = "Equipo Médico"
        verbose_name_plural = "Equipos Médicos"

class Mantenimiento(models.Model):
    TIPOS_MANTENIMIENTO = [
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
        ('calibracion', 'Calibración'),
    ]

    ESTADOS_MANTENIMIENTO = [
        ('programado', 'Programado'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]

    equipo = models.ForeignKey(EquipoMedico, on_delete=models.CASCADE, related_name='mantenimientos')
    tipo = models.CharField(max_length=20, choices=TIPOS_MANTENIMIENTO, default='preventivo')
    fecha_mantenimiento = models.DateField(verbose_name="Fecha del Mantenimiento")
    tecnico_responsable = models.CharField(max_length=150, verbose_name="Técnico Responsable")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones / Detalles")
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Costo ($)")
    estado = models.CharField(max_length=20, choices=ESTADOS_MANTENIMIENTO, default='programado')

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.equipo.nombre} ({self.fecha_mantenimiento})"

class Incidencia(models.Model):
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta / Urgente'),
    ]
    ESTADO_CHOICES = [
        ('abierta', 'Abierta'),
        ('en_proceso', 'En Proceso'),
        ('resuelta', 'Resuelta'),
    ]

    equipo = models.ForeignKey(EquipoMedico, on_delete=models.CASCADE, related_name='incidencias')
    titulo = models.CharField(max_length=150, verbose_name="Título de la Incidencia")
    descripcion = models.TextField(verbose_name="Descripción de la Falla")
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES, default='media')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='abierta')
    fecha_reporte = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.equipo.nombre}"