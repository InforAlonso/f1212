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
        ('Revisados', 'Revisados'),
        ('EnReparacion', 'En reparación'),
        ('Terminados', 'Terminados'),    )
        #('Entregados', 'Entregados'),       )

    def queryset(self, request, queryset):
        """ Solo quiero del 1 al 4, y por defecto, del 1 al 4 todos """
        q = queryset.filter( estado__lt = 5, estado__gt = 0 )
        if self.value() == 'SinRevisar':
            return q.filter( estado__exact = 1 )
        elif self.value() == 'Revisados':
            return q.filter( estado__exact = 2 )
        elif self.value() == 'EnReparacion':
            return q.filter( estado__exact = 3 )
        elif self.value() == 'Terminados':
            return q.filter( estado__exact = 4 )
        else:
            return q

class EntregadosFilter( admin.SimpleListFilter ):
    title = "equipos ya retirados"
    parameter_name = "estado"
    default_value = None

    def lookups(self, request, model_admin):
        """ Me cansé del filtro, lo hice más simple, que busque solo por estado
        si realmente necesita la fecha, la tiene a un clic de distancia """

        return (('Entregados','Entregados'), )

    def queryset(self, request, queryset):
        if self.value() == 'Entregados':
            return queryset.filter( estado__exact = 5 )
        else:
            return queryset.exclude( estado__exact = 5 )

class TrabajoAdmin( admin.ModelAdmin ):
    list_display = [ 'descripcion' ]
    fields = [ 'descripcion' ]

class TrabajoDeTallerAdmin( admin.ModelAdmin ):
    list_display = [ 'fecha_de_inicio', 'equipo', 'estado' ]
    fieldsets = [
    ('Fechas', { 'fields':['fecha_de_inicio','fecha_estimada','fecha_de_fin']}),
    ('Datos del trabajo',{'fields':['equipo','trabajo','estado']}),
    ]
    list_filter = [ 'estado', 'fecha_de_inicio', ]
    search_fields = [ 'equipo__dueño' ]

admin.site.register(Trabajo, TrabajoAdmin)
admin.site.register(TrabajoDeTaller, TrabajoDeTallerAdmin)
