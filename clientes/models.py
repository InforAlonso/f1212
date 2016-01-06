from django.db import models

class Cliente( models.Model ):
    A = "A"
    B = "B"
    C = "C"
    TIPOS_DE_FACTURAS = ((A, "Factura tipo A"),(B, "Factura tipo B"),(C, "Factura tipo C"))

    apellido = models.CharField( max_length = 50 )
    nombre = models.CharField( max_length = 50 )
    nombre_fiscal = models.CharField( max_length = 100, null = True, blank = True )
    direccion_fiscal = models.CharField( max_length = 100, null = True, blank = True )
    cuit = models.CharField( max_length = 20, null = True, blank = True )
    tipo_de_factura = models.CharField( max_length = 1, choices = TIPOS_DE_FACTURAS, null = True, blank = True )

    def __str__(self):
        aux =  self.apellido + ", " + self.nombre
        return aux

class Equipo( models.Model ):
    PC = "PC"
    NOTE = "Note"
    NET = "Net"
    TAB = "Tab"
    IMPR = "Impr"
    TIPOS_DE_EQUIPOS = ((PC,"PC de escritorio"),(NOTE,"Notebook"),(NET,"Netbook"),(TAB,"Tablet"),(IMPR,"Impresora"))

    tipo_de_equipo = models.CharField( max_length = 4, choices = TIPOS_DE_EQUIPOS )

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

    def __unicode__(self):
        return self.tipo_de_equipo + " - " + self.dueño
