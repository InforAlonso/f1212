from django.db import models

# Create your models here.

class Cotizacion(models.Model):

	#Me parece medio calculable, tendr que impactarse en la base de datos??

	#queda chanta si por js despues llama algun api rest para que le pase el valor del día
	dolar = models.DecimalField( max_digits = 5, decimal_places = 2 )
	#creo que cobran un 10% de recrgo
	recargo_porcentual = models.DecimalField( max_digits = 5, decimal_places = 2 )
	precio_en_dolar = models.DecimalField( max_digits = 10, decimal_places = 2 )
	#calculable, es necesario?
	precio_recargado = models.DecimalField( max_digits = 10, decimal_places = 2 )

	def obtener_precio_recargdo(self):
		incrementado_porcentual = ( dolar * precio_en_dolar ) * ( recargo_porcentual / 100 )
		return ( dolar * precio_en_dolar ) + incrementado_porcentual

	# te hace mas comoda la visulizacion en el admin
	def __str__(self):
		return obtener_precio_recargdo()

class Producto(models.Model):
	codigo = models.CharField( max_length = 20 )
	nombre = models.CharField( max_length = 50 )
	rubro = models.CharField( max_length = 50 )
	cantidad = models.IntegerField()
	precio = models.ForeignKey( 'Cotizacion', on_delete = models.CASCADE, )

	def __str__(self):
		return self.nombre
