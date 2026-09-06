from django.db import models

class Incidencia(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En Proceso'),
        ('RESUELTA', 'Resuelta'),
    ]

    PRIORIDADES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
        ('CRITICA', 'Crítica'),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    equipo = models.CharField(max_length=100)
    prioridad = models.CharField(max_length=10, choices=PRIORIDADES, default='MEDIA')
    estado = models.CharField(max_length=15, choices=ESTADOS, default='PENDIENTE')
    fecha_reporte = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.estado}"