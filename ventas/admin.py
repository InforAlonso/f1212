from django.contrib import admin
from ventas.models import Cotizacion, Producto

class CotizacionInline(admin.TabularInline):
    model = Cotizacion
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    list_display = []
    fieldset = []
    list_filter = []
    search_field = []
