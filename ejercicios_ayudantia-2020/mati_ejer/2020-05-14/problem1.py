

enunciado = '''
Implemente en Python la funcion merge(A,B,comp=cmp), pero en lugar de devolver explcitamente la
mezcla en una lista, devuelve una generacion de (o define una forma de generar o iterar) los elementos de la mezcla.
'''

def cmp(a,b): # definimos cmp para los enteros ya que cmp es una funcion estandar en python 2 y no en python 3
    if (a<b):
        return -1
    if (a>b):
        return 1
    else:
        return 0

# range es una funcion con 1 a 3 argumentos; range(e), range(s,e), range(s,e,p)
# los valores default para s y p son 0 y 1
# 's' denota el primer valor, 'e' denota el limite excluyente, y 'p' cuantos numeros se "salta" cada iteracion
# ejemplos: range(3)=>0,1,2. range(2,4)=>2,3. range(1,6,2)=>1,3,5. range(9,2,-2)=>9,7,5,3.
A = range(1,10,2)
B = range(0,11,2)
def merge(A,B,comp=cmp): # A y B son listas, comp debe ser una funcion de comparacion=> igual = 0, mayor = 1, menor = -1
    ia, ib = 0, 0
    la, lb = len(A), len(B)
    while(ia<la and ib<lb):
        if cmp(A[ia],B[ib]) == 1: # vamos entregando en orden los menores numeros
            yield B[ib]
            ib += 1
        else:
            yield A[ia]
            ia += 1
    while(ia<la): # si es que la lista B se vacio, vaciar la lista A tambien
        yield A[ia]
        ia += 1
    while(ib<lb): # si es que la lista A se vacio, vaciar la lista B tambien
        yield B[ib]
        ib += 1

for elemento in merge(A,B):
    print(elemento)

# aprovechamos de definir mergesort dado que es simple en comparacion a merge
def mergesort(A):
    la = len(A)
    if (la == 1): # este es el caso base bajo el planteamiento: una lista de largo 1 esta ordenada
        return A
    A1 = mergesort(A[:(la//2)]) # A[:m] es la parte de la lista con indice 0 <= i <= m-1
    A2 = mergesort(A[(la//2):]) # A[m:] es la parte de la lista con indice m <= i ...
    return list(merge(A1,A2)) # la funcion merge nos entrega un generador, pero por
                              # temas de recursividad, mergesort debe entregar una lista
# si se quiere evitar el uso de list, merge debiera aceptar generadores tambien

# print(mergesort([1,0,4,5,3,7,8,6]))
