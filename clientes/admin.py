from django.contrib import admin
from clientes.models import Equipo, Cliente

# Register your models here.
class EquipoInline(admin.StackedInline):
    model = Equipo
    extra = 1
    fieldsets = [
    ('Notebooks',{'fields' : ['es_notebook','fabricante', 'modelo']}),
    ('Datos del equipo', {'fields': ['procesador', 'placa_madre', 'memorias', 'discos'], 'classes' : ['collapse']}),
    ('Datos extras', {'fields' : ['lectora', 'gabinete', 'placa_de_video','extras'], 'classes' : ['collapse']})
    ]

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['apellido','nombre']
    fieldsets = [
        ('Datos básicos', {'fields':[ 'apellido', 'nombre'],'classes':['wide']}),
        ('Datos de contacto', {'fields':['email', 'nro_de_telefono'],'classes':['wide']}),
        ('Información fiscal', {'fields':['cuit', 'cuil'],'classes':['collapse']})    ]
    list_filter = ['apellido','nombre']
    search_fields = ['apellido','nombre']
    inlines = [EquipoInline]


admin.site.register(Equipo)
admin.site.register(Cliente, ClienteAdmin)
