from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self,id,capacidad,es_disponible,tipo,cant_combustible,patente):
        super().__init__(id,capacidad,es_disponible)
        self.tipo = tipo
        self.cant_combustible = cant_combustible
        self.patente = patente



