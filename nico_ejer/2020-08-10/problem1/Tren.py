from Vehiculo import Vehiculo

class Tren(Vehiculo):
    def __init__(self,id,capacidad,es_disponible,cant_vagon):
        super().__init__(id,capacidad,es_disponible)
        self.cant_vagon = cant_vagon


