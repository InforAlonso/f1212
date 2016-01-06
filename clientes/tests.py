from django.test import TestCase

# Create your tests here.
def crear_cliente(self, apellido_, nombre_):
    """Crea un cliente con datos minimos requeridos por el sistema con fines de
    prueba, unicamente"""
    return Cliente.objects.create( apellido = apellido_, nombre = nombre_ )
def crear_equipo():
    """Crea un equipo y lo asocia a un cliente existente, solo existente en el
    ambiente de pruebas"""

class ClienteTestCase(TestCase):
    """Destinado a testear el api de objetos en la clase Cliente"""
    pass

class EquipoTestCase(TestCase):
    """Destinado a testear el api de objetos en la clase Equipo"""
    pass
