from django.db import models

# Create your models here.

class Cliente( models.Model ):
    apellido = models.CharField( max_length = 50 )
    nombre = models.CharField( max_length = 50 )
    nro_de_telefono = models.CharField( max_length = 36, null = True, blank = True )
    email = models.EmailField( null = True, blank = True )
    cuit = models.CharField( max_length = 20, null = True, blank = True )
    cuil = models.CharField( max_length = 20, null = True, blank = True )

    def __str__(self):
        aux =  self.apellido + ", " + self.nombre
        return aux

class Equipo( models.Model ):
    es_notebook = models.BooleanField()
    fabricante = models.CharField( max_length = 20, null = True, blank = True )
    modelo = models.CharField( max_length = 20, null = True, blank = True )
    procesador = models.CharField( max_length = 30, null = True, blank = True )
    placa_madre = models.CharField( max_length = 30, null = True, blank = True )
    memorias = models.CharField( max_length = 30, null = True, blank = True )
    discos = models.CharField( max_length = 30, null = True, blank = True )
    lectora = models.CharField( max_length = 30, null = True, blank = True )
    gabinete = models.CharField( max_length = 30, null = True, blank = True )
    placa_de_video = models.CharField( max_length = 30, null = True, blank = True )
    extras = models.TextField ( null = True, blank = True )
    dueño = models.ForeignKey( 'Cliente', on_delete = models.CASCADE, )

    def __str__(self):
        if self.es_notebook == True:
            return self.fabricante + " " + self.modelo
        else:
            return self.procesador
