from django.contrib import admin
from caja.models import Motivo, Movimiento, Caja

class MotivoAdmin(admin.ModelAdmin):
    search_fields = [ 'detalle' ]
    list_filter = ['multiplicador']

class MovimientosAdmin(admin.ModelAdmin):
    list_display = [ 'caja', 'motivo', 'fecha' ]
    fieldsets = [
        ( 'Caja del día', { 'fields' : ['caja'] } ),
        ( 'Movimiento', { 'fields' : ['fecha','motivo', 'monto'] } )        ]
    list_filter = [ 'fecha','motivo' ]
    search_fields = [ 'caja__fecha_inicio','caja__esta_cerrada' ]

class CajaAdmin(admin.ModelAdmin):
    list_display = [ 'fecha_inicio', 'esta_cerrada', 'fecha_cierre' ]
    fieldsets = [
        ( 'Apertura', { 'fields' : [ 'fecha_inicio', 'existencia' ] } ),
        ( 'Cierre', { 'fields': [ 'esta_cerrada', 'fecha_cierre' ] } )      ]
    list_filter = [ 'fecha_inicio', 'esta_cerrada' ]
    search_fields = [ 'fecha_inicio' ]

admin.site.register(Motivo, MotivoAdmin)
admin.site.register(Movimiento, MovimientosAdmin)
admin.site.register(Caja, CajaAdmin)
