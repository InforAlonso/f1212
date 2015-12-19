# El encare
Creo que vamos a necesitar, partiendo desde el punto 4 que se ve más fácil que los otros:
Una tabla `cliente` con los datos de la planilla de taller.
Una tabla de `equipo`, con una clave foránea a `cliente`, datos del equipo también en la planilla.

## Punto 2, otro fácil:
CRUD de caja, con una posibilidad de acceder desde las otras aplicaciones
¿Llevamos un registro completo de movimientos, o escalaría muy grande?
Se me ocurre sino, que exista una tabla temporal de movimientos diarios y que al final del día o de la semana, se aplanen en una sola cifra. Se que no es correcto para registros contables, pero esto hay que preguntarlo
¿El detalle lo ponemos como fijos en una tabla aparte?

## Punto 1:
Hará falta la información del proveedor?
No me quedan claras algunas cosas, si quiere que se actualice la lista de objetos sola( tendra un api? No creo)
En todo caso, si no se actualizan, lo del precio no me suena muy útil, salvo cuando vendes para registrarlo en caja
Una tabla de `producto`, con una cantidad entera que representaría la existencia del producto.
Posible tabla de `proveedores` a donde se referencia el `producto`, para hacer más fácil encontrarlo
Una tabla de `producto a vender`, para modelar los `productos` que te seña un `cliente` y congela el precio para después terminar de hacer la compra o encargos, acá te viene genial la tabla de `clientes`. Me imagino, que vez una onda de perfil del tipo y vez que encargó, cuanto te dio y en cuanto fijaron el precio; también debería impactar en la tabla de `caja`

##Punto 3:
Acá es donde veo más trabajo.
Una tabla del `estado del trabajo`.
Una tabla de `causas de problema` o `diagnóstico`, con valores genéricos de cuanto demoraría (esto dijo que lo quería, el TOP 10 de problemas y cuanto demoraría) Esto es fácil, un texto, un delta de tiempo y un contador de ocurrencias para armar el top 10
Una tabla de `trabajo de taller`, con una fecha que el default sea now(), una fecha que pueda ser null para el trabajo terminado, una referencia al `estado del trabajo`. La existencia del estado “entregado” me hace creer que también se van a guardar todos los registros, no se que tan práctico pueda ser ( mientras se mantengan con una cantidad de diagnósticos razonables, esta todo bien, pero si para cada trabajo hacen una entrada en `diagnóstico` distinta, esta todo mal).
Y por último una relación al `cliente`, para buscarlo más rápido. O bien, al `equipo` que ya estaría relacionado con `cliente`.

Hay que pensar que si esto se backupea a dropbox, cada inserción genera una subida completa de la base de datos al final del día y por ahí no esta tan tan bueno si la base de datos escaló mucho. Argentina es una cagada con la velocidad de subida
