# Tenemos dos opciones, guardar las aristas como matrices o como lista de adyacencia,
# para esta implementacion se hara algo asi como un mixto, con listas de adyacencias
# pero para cada vertice, en un diccionario con la key siendo cada vertice y la lista
# el value correspondiente, por lo que se recorre por vertice-key como una matriz, pero
# se guardan listas para representar las aristas para cada vertice
from abc import ABC, abstractmethod

class Graph(ABC): # Comenzamos con una clase abstracta que contenga los metodos comunes para cualquier tipo de grafos
    @abstractmethod
    def __init__(self, Vertices=None, Edges=None): # Dejamos la inicializacion abstracta ya que sera distinto para Grafo dirigidos o no..
        self.GraphDict = {}

    def __repr__(self): # repr y str nos ayudara a visualizar cuando se declara o imprime la variable, suelen ser valores similares
        return self.__str__()

    def __str__(self): # Mostraremos el grafo como suele ser representado en academia, como su lista de adyacencia* ..
        sh = ""        # pero para cada vertice se presentaran los que son adyacente de manera similar a la que esta construida en el objeto
        for key in self.GraphDict:
            sh += str(key) + ": " + ''.join([", "+str(edge) if edge != self.GraphDict[key][0] else str(edge) for edge in self.GraphDict[key]]) + "\n"
        return sh

    def add_vertice(self, vertice): # La agregacion de vertices es comun para cualquier tipo, ya que estos se distinguen solo en las aristas
        if vertice not in self.GraphDict.keys():
            self.GraphDict[vertice] = []
            return True
        return False

    @abstractmethod # Abstracto debido a lo dicho en add_vertice
    def add_edge(self, edge):
        pass

    # Para entender mejor las siguientes funciones es mejor ver los inicializadores de las clases no abstractas...


    # Como tendremos diccionarios de la forma {vertice_1: [vert_ady_1_1, vert_ady_1_2,...],...} para ambos grafos, podemos aplicar el mismo algoritmo para ambos tipos de grafos
    def path(self, start, end):
        if start not in self.GraphDict.keys() or end not in self.GraphDict.keys():
            return None # Caso en que nos fueran a entregar datos invalidos (vertices no existentes)
        return self.__path_aux__(start, end, []) # llamamos funcion auxiliar, se espera siempre fuera de la recursividad con visited como lista vacia

    def __path_aux__(self, start, end, visited): # Agregamos la variable visited para aumentar levemente la eficiencia; con seguridad existen mejores algoritmos!
        if start == end: # Sera una funcion recursiva que se armara una ves encontrado el nodo final, y se desenvolvera su recursividad para agregar el resto del camino
            return [end]
        visited.append(start)
        for dif in self.GraphDict[start]:
            if dif not in visited:
                difres = self.__path_aux__(dif, end, visited) # Llamada recursiva para intentar encontrar algun camino valido
                if difres != None: # Significa que se llego hasta el final, y la funcion empezo desde el inicio, por lo que nos encontramos en un camino valido
                    return [start]+difres
        return None # Se desecha el nodo ya que no se puede llegar hasta el final desde aca

    def connected_subgraphs(self):
        visited_vertices, missing_vertices, current_visited, subcon = [], [vert for vert in self.GraphDict.keys()], [], []
        while len(missing_vertices): # Mientras queden nodos libres
            current_visited = [missing_vertices.pop(0)] # Comenzamos este grupo de vertices conexos con el primero de la lista
            cont = True
            while cont:
                cont = False # Si es que no se agregan en una pasada, significa que ya tenemos nuestro grupo conexo completo
                for vertice in current_visited:
                    for edge in self.GraphDict[vertice]: # Para cada posible nuevo vertice
                        if edge not in current_visited and edge not in visited_vertices: # Dado que aun no se halla agregado a algun grupo
                            cont = True
                            missing_vertices.remove(edge)
                            current_visited.append(edge)
            subcon.append([vert for vert in current_visited]) # Agregamos el conjunto conexo
            while len(current_visited):
                visited_vertices.append(current_visited.pop(0))
        return subcon # retornamos el conjunto de conjuntos conexos (lista de listas de vertices)
                  
                    


class DGraph(Graph): # Grafos dirigido, cada arista puede tener 1 o 2 direcciones (que se pudiera entende como aristas distintas las que van del vertice a al b que las del b al a, etc)
    def __init__(self, Vertices=None, Edges=None): # Inicializacion atraves de un inicializador de diccionarios, pudieramos comenzar un diccionario vacio y agregar elemento a elemento con nuestro metodos especificos tambien
        if Vertices != None:
            if Edges != None: # Usamos comprension de lista y el metodo de inicializacion de diccionarios para que de forma succinta conseguir un diccionario valido de grafo
                self.GraphDict = dict([(v, [pair[1] for pair in Edges if v == pair[0]]) for v in Vertices]) # Dado que es un grafo dirigido, cada arista produce un elemento de adyacencia
            else: # Si nos fueran a entregar solo los vertices sera un grafo sin aristas
                self.GraphDict = dict([(v, []) for v in Vertices])
        else: # Si nos fueran a entregar valores vacios, iniciamos un diccionario vacio para representar que no hay vertices (y por consecuencia no aristas tampoco)
            self.GraphDict = {} # Un valor None tambien denotaria que no hay un grafo, pero el metodo de agregar vertice debiese cambiar para cubrir este caso extra!

    def add_edge(self, edge): # De la misma forma, una arista agregada significa un dato agregado al diccionario
        if edge[0] in self.GraphDict.keys() and edge[1] in self.GraphDict.keys(): # Solo pueden haber aristas si los vertices ya estan presentes
            if edge[0] not in self.GraphDict[edge[1]]: # Dado que aun no este representada
                self.GraphDict[edge[1]].append(edge[0])
                return True
        return False


class UGraph(Graph): # Grafos no dirigido, las aristas no tienen direccion, o se puede representar como un grafo direccional donde todas las aristas tienen su par inverso (si existe (a,b) <=> (b,a))
    def __init__(self, Vertices=None, Edges=None): # Mismo concepto que en DGraph
        if Vertices != None:
            if Edges != None: # cambia la implementacion dado que cada arista agrega 2 elementos, en [a] se agrega b y en [b] se agrega a
                self.GraphDict = dict([(v, [e[1] if e[0] == v else e[0] for e in [edge for edge in Edges if v in edge]]) for v in Vertices])
            else:
                self.GraphDict = dict([(v, []) for v in Vertices])
        else:
            self.GraphDict = {}

    def add_edge(self, edge):
        if edge[0] in self.GraphDict.keys() and edge[1] in self.GraphDict.keys():
            if edge[0] not in self.GraphDict[edge[1]]: # Aqui se ve de forma mas directa, por cada arista, 2 elementos
                self.GraphDict[edge[0]].append(edge[1])
                self.GraphDict[edge[1]].append(edge[0])
        return False

def demo(opt):
    Ver1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    UEdg1 = [['a', 'b'], ['a', 'c'], ['a', 'f'], ['b', 'f'], ['d', 'g'], ['e', 'g']]
    DEdg1 = [['a', 'b'], ['a', 'c'], ['a', 'f'], ['b', 'e'], ['c', 'a'], ['d', 'g'], ['e', 'g'], ['f', 'g'], ['g', 'a'], ['g', 'c'], ['g', 'd']]

    U1 = UGraph(Vertices=Ver1, Edges=UEdg1)
    D1 = DGraph(Vertices=Ver1, Edges=DEdg1)
    pa, pb = 'a', 'd'
    U1_SG = U1.connected_subgraphs()
    D1_P = D1.path(start=pa, end=pb)

    limiter = "-----------------"
    print(limiter)
    print("U1 = UGraph(", Ver1, "\n,", UEdg1, ")\n:=\n",U1)
    print(limiter)
    print("U1.connected_subgraphs() := ", U1_SG)
    print(limiter)
    print(limiter)
    print("D1 = DGraph(", Ver1, "\n,", DEdg1, ")\n:=\n",D1)
    print(limiter)
    print("D1.path(start='a', end='d') :=", D1_P)


inp=None
if __name__ == "__main__":
    demo(opt=inp)
