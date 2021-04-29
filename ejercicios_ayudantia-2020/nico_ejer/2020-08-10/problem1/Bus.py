from Vehiculo import Vehiculo

class Bus(Vehiculo):
    def __init__(self,id,capacidad,es_disponible,cant_combustible,cant_piso,patente):
        super().__init__(id,capacidad,es_disponible)
        self.cant_combustible = cant_combustible
        self.cant_piso = cant_piso
        self.patente = patente