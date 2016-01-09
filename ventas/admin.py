from django.contrib import admin
from ventas.models import Venta, MiProducto, RelacionDeVenta, MiCliente

class RelacionDeVentaInline(admin.TabularInline):
    model = RelacionDeVenta
    extra = 1
    fields = ('producto', 'cantidad', )

class VentaAdmin(admin.ModelAdmin):
    list_display = ['fecha_de_venta', 'cliente']
    inlines = [RelacionDeVentaInline]
    fieldsets = [
    ( 'Datos de cliente', { 'fields' : [ 'cliente' ] } ),
    ( 'Datos de la venta', { 'fields' : [ 'fecha_de_venta', 'dolar', 'monto_total' ] } ) ]
    list_filter = ['fecha_de_venta']
    search_field = ['fecha_de_venta','cliente']

#admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)
