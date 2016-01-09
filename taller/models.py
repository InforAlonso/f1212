from django.db import models
from clientes.models import Equipo
from django.utils import timezone

class Trabajo( models.Model ):
    descripcion = models.CharField( max_length = 100 )
    ranking = models.PositiveIntegerField( default = 0 )

    class Meta:
        ordering = ["-ranking"]

    def __str__(self):
        return self.descripcion

class MiEquipo( Equipo ):
    class Meta:
        proxy = True

class TrabajoDeTaller( models.Model ):
    SIN_REVISAR = 1
    REVISADO = 2
    EN_REPARACION = 3
    TERMINADO = 4
    ENTREGADO = 5

    ESTADOS = (
    (SIN_REVISAR, "Equipo pendiente de revisión"),
    (REVISADO, "Equipo pendiente de reparación"),
    (EN_REPARACION, "Equipo en proceso de reparación"),
    (TERMINADO, "Equipo terminado"),
    (ENTREGADO, "Equipo retirado"),    )

    fecha_de_inicio = models.DateTimeField( default = timezone.now )
    fecha_estimada = models.DateTimeField( null = True, blank = True )
    fecha_de_fin = models.DateTimeField( null = True, blank = True )
    estado = models.PositiveSmallIntegerField( choices = ESTADOS, default = SIN_REVISAR )
    equipo = models.ForeignKey( "MiEquipo", on_delete = models.CASCADE )
    trabajo = models.ForeignKey( "Trabajo", on_delete = models.CASCADE )

    def __str__(self):
        return "%s, %s - %s" % ( self.equipo, self.equipo.dueño, self.trabajo )

    class Meta:
        verbose_name_plural = "Trabajos de taller"
