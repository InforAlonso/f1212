from django.contrib import admin
from taller.models import Trabajo, TrabajoDeTaller
from datetime import datetime, timedelta

class EnElLocalFilter( admin.SimpleListFilter ):
    title = "equipos en el taller"
    parameter_name = "estado"
    default_value = None

    def lookups(self, request, model_admin):
        return (
        ('SinRevisar', 'Sin revisar'),
        ('Revisado', 'Revisados'),
        ('EnRepación', 'En reparación'),
        ('Terminado', 'Terminados'),        )

    def queryset(self, request, queryset):
        q = queryset.filter( estado__lt = 5 )
        if self.value() == 'SinRevisar':
            return q.filter( estado = 1 )
        elif self.value() == 'Revisado':
            return q.filter( estado = 2 )
        elif self.value() == 'EnReparación':
            return q.filter( estado = 3 )
        elif self.value() == 'Terminado':
            return q.filter( estado = 4 )
        else:
            return q

class EntregadosFilter( admin.SimpleListFilter ):
    title = "equipos ya retirados"
    parameter_name = "estado"
    default_value = None

    def lookups(self, request, model_admin):
        return (
        ('Hoy', 'Hoy'),
        ('Últimos7Días', 'Últimos 7 días'),
        ('EsteMes', 'Este mes'),
        ('EsteAño', 'Este año'),
        ('Todos', 'Todos los equipos entregados')
        )

    def queryset(self, request, queryset):
        q = queryset.filter( estado = 5 )
        hoy = datetime.today()
        hace_7_dias = hoy - timedelta(days=-7)
        if self.value() == 'Hoy':
            return q.filter( fecha_de_inicio__date = hoy.date() )
        elif self.value() == 'Últimos7Días':
            return q.filter( fecha_de_inicio__gte = hace_7_dias )
        elif self.value() == 'EsteMes':
            return q.filter( fecha_de_inicio__month = hoy.month, fecha_de_inicio__year = hoy.year )
        elif self.value() == 'EsteAño':
            return q.filter( fecha_de_inicio__year = hoy.year )
        elif self.value() == 'Todos':
            return q
        else:
            return queryset

class TrabajoAdmin( admin.ModelAdmin ):
    list_display = [ 'descripcion' ]
    fields = [ 'descripcion' ]

class TrabajoDeTallerAdmin( admin.ModelAdmin ):
    list_display = [ 'fecha_de_inicio', 'equipo', 'estado' ]
    fieldsets = [
    ('Fechas', { 'fields':['fecha_de_inicio','fecha_estimada','fecha_de_fin']}),
    ('Datos del trabajo',{'fields':['equipo','trabajo','estado']}),
    ]
    list_filter = [ EnElLocalFilter, 'fecha_de_inicio', EntregadosFilter, ]
    search_fields = [ 'equipo__dueño' ]

admin.site.register(Trabajo, TrabajoAdmin)
admin.site.register(TrabajoDeTaller, TrabajoDeTallerAdmin)
