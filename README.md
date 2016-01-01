# f1212
## Requerimientos
Sistema de gestión de local de informática

1. **Stock**
	* Debe poder contabilizar cuanto de cada cosa se pidió a proveedor,
	* Cuánto se recibió y precio de compra,
	* Cuánto se vendió
	* Cálculo de precio distribuidor/valor dólar
	* Cálculo de recargo por producto
2. **Arqueo de caja**
	* Cuánto hay en caja al comenzar el día,
	* Cuánto ingreso por ventas
	* Cuánto se retiró, incluido extracciones para impuestos ( movimientos de caja + una descripción )
3. **Taller**
	* Ingreso se nuevas órdenes al taller
	* Costo presupuestado y costo real
	* Tiempo estimado de trabajo y tiempo real trabajado
	* Estado (a presupuestar, trabajando, terminado, entregado)
	* agregar alarmas y recordatorios
4. **Clientes**
	* Manejo de datos de clientes y sus equipos para facilitar la identificación de los mismos

## Model de persistencia
[Así lo encararía yo](https://github.com/InforAlonso/f1212/blob/master/documentacion/como_yo_lo_encararia.md)
[El encare segundo](https://github.com/InforAlonso/f1212/blob/master/documentacion/el_encare_segundo.md)
