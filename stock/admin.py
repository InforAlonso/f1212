from django.contrib import admin
from stock.models import Rubro, Producto

class DisplonibleFilter(admin.SimpleListFilter):
    """ Clase de filtro, es extraño, quise usar boolenaos en los valores no
    humanos pero no me dejaba, me los parsea como string y después me lo compara
    en el if string contra un booleano y siempre da True al menos que pase una
    string vacía y es algo criptico y dificil de entender, asi que paso Si y No
    para que sea un poco más entendible para el usuario final que va la URL """

    title = "disponibilidad"
    parameter_name = "disponible"
    default_value = None

    # Lamentablemente seran strings aunque ensucien la simplicidad
    def lookups(self, request, model_admin):
        return ( ( 'Si', "Disponible" ), ( 'No', "No disponible" ) )

    def queryset(self, request, queryset):
        if self.value() == 'Si':
            return queryset.filter( cantidad__gt = 0 )
        elif self.value() == 'No':
            return queryset.filter( cantidad__exact = 0 )
        return queryset

class RubroAdmin(admin.ModelAdmin):
    list_display = [ 'nombre' ]
    search_fields = [ 'nombre' ]

class ProductoAdmin(admin.ModelAdmin):
    list_display = [ 'nombre', 'precio_incrementado', 'disponibilidad' ]
    list_filter = [ DisplonibleFilter, 'tipo_de_iva', ]
    search_fields = [ 'nombre' ]
    fieldsets = [
        (None, {'fields' : [ 'nombre' ] } ),
        (None, {'fields' : [ 'precio', 'tipo_de_iva', 'incremento' ] } ),
        (None, {'fields' : [ 'cantidad', 'rubro' ] } ),        ]

admin.site.register(Rubro, RubroAdmin)
admin.site.register(Producto, ProductoAdmin)
