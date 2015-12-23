from django.db import models

# Create your models here.

class Cotizacion(models.Model):
	dolar = models.DecimalField(max_digits = 5, decimal_places = 2, null = False, blank = False)
	recargo_porcentual = models.DecimalField(max_digits = 5, decimal_places = 2)
	precio_en_dolar = models.DecimalField(max_digits = 10, decimal_places = 2, null = False, blank = False)
	precio_recargado = models.DecimalField(max_digits = 10, decimal_places = 2)

	def __str__(self):
		recargo_pesos = ((dolar * precio_en_dolar) * recargo_porcentual)/100
		precio_recargado = (dolar * precio_en_dolar) + recargo_pesos
		return precio_recargado

class Producto(models.Model):
	codigo = models.CharField( max_length = 20, null = False, blank = False )
	nombre = models.CharField( max_length = 50, null = False, blank = False )
	rubro = models.CharField( max_length = 50, null = False, blank = False )
	cantidad = models.CharField( max_length = 10, null = False, blank = False )
	precio = models.ForeignKey( 'Cotizacion', on_delete = models.CASCADE, )

def __str__(self):
	return Producto