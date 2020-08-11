from ListaVehiculo import ListaVehiculo

class EmpresaTransporte():
    def __init__(self,nombre,direccion,email):
        self.nombre =nombre
        self.direccion = direccion
        self.email = email
        self.lista_vehiculo = ListaVehiculo()



if __name__ == "__main__":
    E = EmpresaTransporte('e1','av123','a@b.c')
    print(E.nombre,E.direccion,E.email)
    