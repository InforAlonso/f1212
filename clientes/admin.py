from django.contrib import admin
from clientes.models import Equipo, Cliente

# InLine de Equipo, para registrar un equipo al mismo tiempo que se registra un cliente
class EquipoInline(admin.StackedInline):
    model = Equipo
    #se puede registrar 1 o más, pero es raro que caigan con muchas computadoras de una
    extra = 1
    fieldsets = [
    ('Notebooks',{'fields' : ['es_notebook','fabricante', 'modelo']}),
    ('Datos del Hardware', {'fields': ['procesador', 'placa_madre', 'memorias', 'discos','lectora', 'gabinete', 'placa_de_video'], 'classes' : ['collapse']}),
    ('Datos extras', {'fields' : ['extras'], 'classes' : ['collapse']})
    ]

class ClienteAdmin(admin.ModelAdmin):
    #Ordena los datos en la tabla de los clientes del panel de administración
    list_display = [ 'apellido', 'nombre' ]
    #Modela como se ven los datos en el registro o edición del cliente
    fieldsets = [
        ('Datos básicos', {'fields':[ 'apellido', 'nombre'],'classes':['wide']}),
        ('Datos de contacto', {'fields':['email', 'nro_de_telefono'],'classes':['wide']}),
        ('Información fiscal', {'fields':['cuit', 'cuil'],'classes':['collapse']})    ]
    #va a crear una entrada de filtro por cada cliente y no sirve
    #list_filter = ['apellido','nombre']
    #parámetros del cuadro de busqueda, a más parámetros, más densa la busqueda
    #el caracter ^ hace que se busque solo con el comodín detras, ej: john* y no *john*
    search_fields = [ '^apellido', '^nombre' ]
    #No agregar un equipo al agregar un cliente es un poco redundante, pero se puede
    #inline para agregar un equipo al agregar un cliente
    inlines = [EquipoInline]

class EquipoAdmin(admin.ModelAdmin):
    list_display = [ 'dueño', 'es_notebook', '__str__' ]
    fieldsets = [
        (None,{'fields' : ['dueño']}),
        ('Notebooks',{'fields' : ['es_notebook','fabricante', 'modelo']}),
        ('Datos del Hardware', {'fields': ['procesador', 'placa_madre', 'memorias', 'discos','lectora', 'gabinete', 'placa_de_video'], 'classes' : ['collapse']}),
        ('Datos extras', {'fields' : ['extras'], 'classes' : ['collapse']}) ]
    list_filter = [ 'es_notebook' ]
    search_fields = [ '^dueño__apellido','^dueño__nombre' ]

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Cliente, ClienteAdmin)
