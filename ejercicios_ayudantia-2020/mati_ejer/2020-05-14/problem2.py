



enunciado ='''
Implemente en Python la funcion modulo(A,k) que recibe una lista A y un entero positivo k, y
devuelve una lista compuesta por k listas. La lista numero i de la lista resultado contiene de la lista original los
elementos que se encuentran en las posiciones que dejan resto i en la division por k. Por ejemplo, para
A = [0,1,2,3,4,5,6,7,8,9,10] y k = 3, la funcion debe devolver la lista [[0,3,6,9], [1,4,7,10], [2,5,8]].
'''


# funcion similar al conjunto Zn de algebra, se nos pide que devuelva una lista de listas
def modulo(A,k):
    L = []
    for i in range(k): # generamos la lista para cada modulo, #({0,1,..,k-1}) = k
        L.append([])
    for elemento in A: # colocamos cada valor en la lista correspondiente a su modulo con k
        (L[elemento%k]).append(elemento)
    return L

A = [0,1,2,3,4,5,6,7,8,9,10]
k = 3
print(modulo(A,k))
