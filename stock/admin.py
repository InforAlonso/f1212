from django.contrib import admin

class RubroAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_field = ['nombre']

class ProductoAdmin(admin.ModelAdmin):
    list_display = [ 'nombre', 'precio_incrementado', 'disponibilidad' ]
    list_filter = [ 'tipo_de_iva', 'disponibilidad' ]
    search_field = [ 'nombre' ]
    fieldsets = [ 
        (None, {'fields' : ['nombre'] } ),
        (None, {'fields' : ['precio','tipo_de_iva','incremento' ] } ),
        (None, {'fields' : ['cantidad', 'rubro' ] } ),
        ]

admin.site.register(RubroAdmin)
admin.site.register(ProductoAdmin)
