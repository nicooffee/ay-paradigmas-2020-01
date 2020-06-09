import numpy as np
def adyacentes(x,y):
    Ad = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i!= 0 or j!=0 :
                Ad.append((i+x,j+y))
    return Ad

def copy_matrix(M):
    R = []
    for x in M:
        C = []
        for y in x:
            C.append(y)
        R.append(C)
    return R


def esta_dentro(M,i,j):
    return (True if (i>=0 and j>=0) and (i<len(M) and j<len(M[0])) else False)

def paridad(M,i,j):
    R = copy_matrix(M)
    pila = [(i,j)] #1,1
    usada = {}
    while len(pila)>0:
        x,y = pila.pop()           #x,y = 1,1  
        key = '{},{}'.format(x,y)  #key = '1,1'
        if (key not in usada) or not (usada[key]): #si '1,1' no esta en usada
            if esta_dentro(M,x,y): #x,y esta dentro de los rangos de M (y por lo tanto de R)
                R[x][y] = '-' if M[x][y]%2==0 else '*' #Si M[x][y] es par -> '-' si no '*'
                usada[key] = True  #como ya comprobé x,y, lo marco como usado, comprobado
                pila = pila + adyacentes(x,y)
    return R
M = [
    [2,2,0],
    [7,1,4],
    [9,0,3]
]
x,y = 1,1

print(np.matrix(paridad(M,x,y)))