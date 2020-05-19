# 1  0  1
# 1  1  0
# 1  1 -3

# 1  0  1
# 1  1  0 
# 3  3  3 +
# T = [5,4,4]

# x_a,y_a
#
#
#           x_b,y_b

# 1  0  1  
# 1  1  0 i 
# 1  1 -3 lim

# Pruebo cada combinación de la matriz usando las filas, es decir:
# Desde Hasta (filas)
# 0     0
# 0     1
# 0     2
# ...
# 0     n
# ...
# n-1   n
# comprimo tales subbloques en un array y utilizo MSC para sacar su
# subsequencia de suma máxima, es decir, sus limites de columnas.
#      c   d
#    0 1 2 4
# a -2 2 0 6
# b  0 0 1 0 
# en ese ejemplo, la función matrixMSC va probando con cada combinación
# de a,b. Luego, la función arrayMSC entrega los c,d ya que estoy 
# comprimiendo todas las filas desde a hasta b. [-2,2,1,6], entonces la
# suma máxima de ese arreglo está en [2,1,6], que son los c,d que retorno.
#
# La complejidad del algoritmo que se da en el trabajo depende de si los
# a,b iteran en filas o en columnas. Este algoritmo no hace eso y solo toma
# por default las filas.
def matrixMSC(M):
    suma_max = 0 
    x_a,x_b = 0,0
    y_a,y_b = 0,0
    if len(M) == 0:
        return 0,0
    else:
        for i in range(len(M)):
            T = [0]*len(M[i])
            for j in range(i,len(M)):
                for k in range(len(M[i])):
                    T[k] += M[j][k]
                suma,y_a_aux, y_b_aux = arrayMSC(T)
                if suma > suma_max:
                    suma_max,y_a,y_b = suma,y_a_aux,y_b_aux
                    x_a,x_b = i,j
        return suma_max,x_a,x_b,y_a,y_b
        



def arrayMSC(A):
    if len(A) == 0:
        return 0,0
    else:
        i = 0
        j = i
        s = 0
        s_max = 0
        for x in range(len(A)):
            s += A[x]
            if s<0:
                i = x + 1
                s = 0
            if s>s_max:
                j = x
                s_max = s
        return s_max,i,j


A = [[-1,-1,-1,-1],[1,2,3,4],[1,2,3,4]]
# -1 -1 -1 -1
#  1  2  3  4
#  1  2  3 -4
#Kadane:
#  1  2  3
#  1  2  3
s_max,x_a,x_b,y_a,y_b = matrixMSC(A)
print("suma:{} - {},{} -> {},{}".format(s_max,x_a,y_a,x_b,y_b))