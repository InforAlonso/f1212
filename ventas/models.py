from django.db import models
#from stock.models import Producto
from clientes.models import Cliente
from datetime import date
from decimal import *
from stock.models import Producto

""" Lo veo como modelar una clase de Factura, las facturas se libran contra un
cliente. Tienen datos del día que se hacen, contienen renglones o lineas de factura.
Cada linea de factura se vinculan a un producto y su precio unitario, tienen una
cantidad y un subtotal, que sumados y agregados los correspondientes impuestos
dan el monto total de la factura.
Si bien es calculable, es una práctica razonable guardar el total
en la factura, te evita hacer un monton de llamadas a la base de datos si el cliente
hizo una compra de mucha variedad de productos, te evitas, buscar dentro de la
tabla facturas, la factura que queres para tener el id, para buscar dentro de toda
la tabla de lineas de factura, cual se relacionan con esa factura en particular,
y luego buscar todos los productos y empezar a devolver precios, para despues
calcular, y eso si consideras que el precio del producto nunca cambia, si cambia
estas en la lona, por eso necesitas el subtotal dentro de la linea de la factura.
Y de todas maneras te ahorra movimientos y lógica guardar un flotante """

# PROXY MODEL -> es para hacer los llamados cruzados de apps
class MiCliente(Cliente):
	class Meta:
		proxy = True

class HayStock(Producto):
	class Meta:
		proxy = True

class Producto(models.Model):
	""" SUPER PROVISIONAL PARA SILENCIAR EL ERROR DE FALTA DE MODELO(MUY MAL!)"""
	nombre = models.CharField( max_length = 50 )
	precio_en_dolar = models.DecimalField( max_digits = 10, decimal_places = 2 )

	def __str__(self):
		return "%s u$s%.2f" % (self.nombre, self.precio_en_dolar)

class Venta(models.Model):
	# al tener null = True, permito que exista null en la base de datos, pero
	# obligo al usuario a hacer registrar ventas contra un cliente
	# Si elimino el cliente de mi DB no elimino su compra
	cliente = models.ForeignKey( "MiCliente", on_delete = models.SET_NULL, null = True, blank = True )
	# Se calcula en el template, lado del cliente, o en el view, previa a la
	# visualización, mejor no calcularlo en el modelo. Además hay que traer el
	# valor del dolar, y mejor hacerlo con alguna api de monedas y todo eso
	# lista = RelacionDeVenta.objects.filter( venta_id__exact=self.id )
	monto_total = models.DecimalField( max_digits = 10, decimal_places = 2 )
	fecha_de_venta = models.DateField( default = date.today )
	dolar = models.DecimalField( max_digits = 5, decimal_places = 2 )

	def __str__(self):
		return "%s - %s" % (self.fecha_de_venta.strftime("%d %b. %Y"), self.cliente)

class RelacionDeVenta(models.Model):
	# el incremento puede ir aca o en la venta, lo puse aca para poder personalizar
	# cada producto que vende, por ahí es muy cargoso, pero es más flexible
	producto = models.ForeignKey( "Producto", on_delete = models.CASCADE )
	venta = models.ForeignKey( "Venta", on_delete = models.CASCADE )
	cantidad = models.PositiveIntegerField();
	incremento = models.DecimalField( max_digits = 5, decimal_places = 2 )
	subtotal = models.DecimalField( max_digits = 7, decimal_places = 2, null = True)

	def precio_incrementado(self):
		aux = ( Decimal(1) + ( self.incremento / Decimal(100) ) )
		return Decimal(self.producto.precio_en_dolar * aux )

	def calcular_subtotal(self):
		return self.precio_incrementado() * self.cantidad

	def __str__(self):
		return "%s u$s%.2f" % (self.producto.nombre, self.calcular_subtotal())

	def calcular_stock(self):
		aux = cantidad - HayStock.cantidad
		#este retorno no va a quedar, lo dejo asi por ahora por que no se como manejar un popup 
		#para que retorne error
#		if aux > 0:
			return self.cantidad
#		else:
#			return render_to_response('template_name', message='Error, falta Stock')

