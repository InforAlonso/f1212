from django.db import models
from decimal import *

class Rubro( models.Model ):
    nombre = models.CharField( "Nombre del grupo", max_length = 50 )

    def cantidad_de_un_rubro( self, id ):
        return Producto.objects.filter( rubro_id = id ).count()

    def __str__(self):
        return self.nombre + " ("+ self.cantidad_de_un_rubro( self.id ) +")"

class Producto( models.Model ):
    T1 = Decimal(10.5)
    T2 = Decimal(21)
    TIPOS DE IVA = ( ( T1, "IVA de %10,5" ), ( T2, "IVA de %21" ), )
    nombre = models.CharField( max_length = 100 )
    precio = models.DecimalField( max_digits = 7, decimal_places = 2 )
    tipo_de_iva = models.DecimalField( max_digits = 5, decimal_places = 2,
        choices = TIPOS_DE_IVA, default= T2 )
    incremento = models.DecimalField( max_digits = 5, decimal_places = 2,
        help_text = "Acordate de no sumar dos veces el IVA"  )
    cantidad = models.PositiveIntegerField(default = 0)
    rubro = models.ForeignKey( Rubro, on_delete = models.PROTECT )

    def __str__(self):
        return self.nombre

    def disponibilidad(self):
        return self.cantidad > 0

    def precio_incrementado(self):
        aux = self.tipo_de_iva + self.incremento
        aux = Decimal(1) + (aux / Decimal(100))
        return aux * precio

    disponibilidad.boolean = True
    disponibilidad.short_description = "Producto disponible?"
