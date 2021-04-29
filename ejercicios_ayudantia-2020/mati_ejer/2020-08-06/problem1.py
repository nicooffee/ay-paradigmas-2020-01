class Persona: # Clase que representa a una persona generica
    def __init__(self, ide, nom, ed): # Tiene: numero de identidad, nombre y edad. hacemos un inicializador adecuado
        self.__identidad = int(ide) # Guardamos la identidad como variable privada
        self.nombre = nom
        self.edad = int(ed)

    def info(self, end=None): # Mostramos sus datos incluyendo identidad ya que al ser de la clase, es utilizable
        return str(self.__identidad)+" "+self.nombre+" "+str(self.edad)+("\n" if end == None else end)

    def mayor(self, edad):
        return edad > self.edad


class PersonaEstudiante(Persona): # Clase que representa a un estudiante no superior (basica-media: años 1 - 12)
    def __init__(self, ide, nom, ed, an): # Inicializamos con un dato extra, anho en que se encuentra
        super().__init__(ide, nom, ed) # Dejamos que Persona inicializa sus datos
        self.anho = an # solo tenemos que inicializar los nuevos datos

    def info(self, end=None): # Mostramos los datos de persona + anho, el diseño de las funciones info nos permite utilizarlas en conjunto y que sea extensible
        return super().info(" ")+str(self.anho)+ ("\n" if end == None else end)

    def Einfo(self, end=None): # Intentamos replicar la funcion info pero accediendo a los datos desde la clase heredera, falllara ya que __identidad es privada en Persona
        return str(self.__identidad)+" "+self.nombre+" "+str(self.edad)+" "+str(self.anho)+("\n" if end == None else end)

#Demo
print("----Persona----")
print('P = Persona(ide=111132, nom="maria", ed=18)')
P = Persona(ide=111132, nom="matias", ed=18)
print("P.mayor(10): ",P.mayor(10))
print("P.info(): ",P.info())
try:
    print("P.__identidad: ",P.__identidad)
except AttributeError:
    print("Ooops identidad es una variable privada")
print("----Estudiante----")
print('E = PersonaEstudiante(ide=211132, nom="marco", ed=7, an=3)')
E = PersonaEstudiante(ide=211132, nom="marco", ed=7, an=3)
print("E.mayor(10): ",E.mayor(10))
print("E.info(): ",E.info())
try:
    print("E.Einfo(): ",E.Einfo())
except AttributeError:
    print("Ooops Einfo no esta bien definida")
try:
    print("E.__identidad: ",E.__identidad)
except AttributeError:
    print("Ooops identidad es una variable privada")
