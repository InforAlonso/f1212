# Segunda iteración de requerimientos

##Revisión de `clientes`
### Clase Cliente

 1. Descartar CUIL
 2. Descartar todos los datos de contacto
 3. Modificar el nombre y apellido, corresponden al cliente que frecuenta, pero pueden no coincidir contra quien se facturan o la empresa a la que se facturan. Se requiere:
	 - Una discriminación de persona real y persona jurídica
	 - Una dirección fiscal
	 - El CUIT en esta parte de los datos
	 - Tipo de factura que se le emite a la persona jurídica

### Clase Equipo

Mayormente bien, se desea que el filtro de muestra tengo los siguientes filtros:

 - PC de escritorio
 - Notebook
 - Netbook
 - Tablet
 - Impresora

Se puede implementar fácil con la opción de choices dentro de admin.py


----------


##Revisión de `caja`
### Motivos

 - Deberían sumar o restar automaticamente, hay que agregarle un
   multiplicador de +/- 1 en la tabla y que el importe lo multipliquen
   por el multiplicador
 - Pensar como facilitar la selección de motivos, tiene muchos impuestos para pagar, cerca de 40.

### Movimientos
Los quiere discriminados en dos tablas, una de ingresos y otra de salidas, esto es medio imposible para el panel de administración, se delega a la vista y al lado del cliente


----------


## Revisión de `ventas`

 - Se requiere que la venta sume automaticamente los subtotales(ya
   especulado para la vista) Se requiere un "cliente puntitos", por lo
   que la venta puede estar ligada a un cliente nulo
 - Se quiere un orden de campos `producto` `valor en $` `tipo de iva` `cantidad`


----------

## Revisión de `stock`

 - El dólar toma un valor, una vez al día. Esto se sigue pudiendo hacer con la API que encontre, en lugar de pedir un valor current se le pide un valor especifica de tiempo y sería algo como "date.today() a las 9 am" y simulamos que lo toma una vez al día para no guardarlo
 - El producto ya se registra con su respectivo incremento, correspondiente al tipo iva
 - El producto tiene una clave foranea a un "Rubro"
 - El producto tiene un precio en dólar
 - El producto tiene una cantidad que representa el stock interno
 - El producto tiene una disponibilidad (calculable) positiva si cant. < 0
