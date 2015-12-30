from django.db import models
from django.utils import timezone
from datetime import datetime

class Motivo(models.Model):
    detalle = models.CharField( max_length = 150 )
    def __str__(self):
        return self.detalle

class Movimiento(models.Model):
    fecha = models.DateTimeField( default = timezone.now )
    monto = models.DecimalField( max_digits = 8, decimal_places = 2 )
    motivo = models.ForeignKey( 'Motivo', on_delete = models.PROTECT )
    caja = models.ForeignKey('Caja',on_delete = models.PROTECT, limit_choices_to = {'esta_cerrada' : False} )
    #que el limit_choices_to compare con la fecha de cierre y sacar el bool, sería genial

    #aca tengo problemas para representar el texto de la FK
    def __str__(self):
        return self.motivo.detalle

class Caja(models.Model):
    fecha_inicio = models.DateTimeField( )
    fecha_cierre = models.DateTimeField( null = True, blank = True )
    existencia = models.DecimalField( max_digits = 8, decimal_places = 2 )
    esta_cerrada = models.BooleanField( default = False )

    def __str__(self):
        return self.fecha_inicio.strftime("%Y/%m/%d")
