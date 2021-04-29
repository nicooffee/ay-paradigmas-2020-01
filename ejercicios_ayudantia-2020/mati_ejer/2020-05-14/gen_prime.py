# algoritmo de heuristico de fuerza bruta para generar los primeros n primos
def prime(n):
    p = 2 # el primer primo
    np = 0 # cantidad de primos
    while(np < n): #queremos entregar n primos
        for num in range(2, p+1): # recorrer todos los antecesores de p
            if (num == p): #ningun numero menor que p, distinto que 1 es divisor de p => p es primo
                yield p
                np += 1
            if ( p%num == 0 ): # p es compuesto, no se entregara
                break
        p += 1
        
print(list(prime(10)))
