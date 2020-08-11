from abc import ABCMeta,abstractmethod
class Vehiculo(metaclass=ABCMeta):
    def __init__(self,id,capacidad,es_disponible):
        self.id = id
        self.capacidad = capacidad
        self.es_disponible = es_disponible

    def get_id(self):
        return self.id

