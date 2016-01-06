from django.contrib import admin
from ventas.models import Venta, Producto, RelacionDeVenta, MiCliente
#from clientes.models import Cliente

class RelacionDeVentaInline(admin.TabularInline):
    model = RelacionDeVenta
    extra = 1
    fields = ('producto', 'cantidad', 'incremento')

class VentaAdmin(admin.ModelAdmin):
    list_display = ['fecha_de_venta', 'cliente']
    inlines = [RelacionDeVentaInline]
    fieldsets = [
    ( 'Datos de cliente', { 'fields' : [ 'cliente' ] } ),
    ( 'Datos de la venta', { 'fields' : [ 'fecha_de_venta', 'dolar', 'monto_total' ] } ) ]
    list_filter = ['fecha_de_venta']
    search_field = ['fecha_de_venta','cliente']

class ProductoAdmin(admin.ModelAdmin):
    """ PROVISIONAL, DEBE BORRARSE """
    list_display = ['nombre','precio_en_dolar']
    fields = ['nombre','precio_en_dolar']
    search_field = ['nombre']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
